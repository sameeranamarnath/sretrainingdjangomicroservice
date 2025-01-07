from django.urls import path
from .views import HelloWorldView, GenerateReportView,GetEmployeeData,Authenticate

urlpatterns = [
    path('', HelloWorldView.as_view(), name='hello_world'),
    path('getEmployeeData', GetEmployeeData.as_view(), name='getEmployeeData'),
    path('authenticateEmployee', Authenticate.as_view(), name='authenticateEmployee'),
    
    path('generate-report/<int:employee_id>/', GenerateReportView.as_view(), name='generate_report'),
]