from confluent_kafka import Consumer, Producer
from reportlab.pdfgen import canvas
import boto3
from io import BytesIO
import json
from django.conf import settings
from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_django_project.settings')
application = get_wsgi_application()

from .models import EmployeeData

def generate_pdf(employee_id):
    # Fetch employee data
    employee_data = EmployeeData.objects.filter(employee_id=employee_id).first()
    if not employee_data:
        return None

    # Generate PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, f"Employee ID: {employee_data.employee_id}")
    p.drawString(100, 730, f"Check-in: {employee_data.checkin_time}")
    p.drawString(100, 710, f"Check-out: {employee_data.checkout_time}")
    p.drawString(100, 690, f"Hours Spent on Programming: {employee_data.hours_spent}")
    p.showPage()
    p.save()

    # Upload to S3
    buffer.seek(0)
    s3 = boto3.client('s3')
    s3.upload_fileobj(buffer, 'your-s3-bucket-name', f'reports/{employee_id}.pdf')

    return f'reports/{employee_id}.pdf'

def consume():
    consumer = Consumer({
        'bootstrap.servers': 'your_kafka_broker',
        'group.id': 'report_generation_group',
        'auto.offset.reset': 'earliest'
    })

    producer = Producer({'bootstrap.servers': 'your_kafka_broker'})

    consumer.subscribe(['report_requests'])

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        data = json.loads(msg.value().decode('utf-8'))
        employee_id = data.get('employee_id')
        if employee_id:
            pdf_path = generate_pdf(employee_id)
            if pdf_path:
                producer.produce('report_ready', json.dumps({'employee_id': employee_id, 'pdf_path': pdf_path}))
                producer.flush()

    consumer.close()

if __name__ == '__main__':
    consume()