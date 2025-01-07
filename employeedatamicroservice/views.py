from django.http import JsonResponse
from django.views import View
from reportlab.pdfgen import canvas
import boto3
from io import BytesIO
from .models import EmployeeData

class GenerateReportView(View):
    def get(self, request, employee_id):
        # Fetch employee data
        employee_data = EmployeeData.objects.filter(employee_id=employee_id).first()
        if not employee_data:
            return JsonResponse({'error': 'Employee not found'}, status=404)

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

        return JsonResponse({'message': 'Report generated and stored on S3'})


class HelloWorldView(View):
    def get(self, request):
        return JsonResponse({'message': 'new 2 update in Hello  World from django microservice!'})


class GetEmployeeData(View):
    def get(self, request):
        return JsonResponse({'QPS': '95%', 'Benefits':["401k","MedicalInsurance","CompanySponsoredTrips"],"PerformanceReviewScore":"80%"})

class Authenticate(View):
    def get(self, request):
        return JsonResponse({'Authenticated': 'true' })