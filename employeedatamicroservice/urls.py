from django.urls import path
from .views import HelloWorldView, GenerateReportView

urlpatterns = [
    path('', HelloWorldView.as_view(), name='hello_world'),
    path('generate-report/<int:employee_id>/', GenerateReportView.as_view(), name='generate_report'),
]