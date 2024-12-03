from django.db import models

class EmployeeData(models.Model):
    employee_id = models.IntegerField(unique=True)
    employee_name = models.TextField()
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField()
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Employee id:{self.employee_id} name:{self.employee_name}"