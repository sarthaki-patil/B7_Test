from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    exp = models.IntegerField()
    address = models.CharField(max_length = 255)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return f"{self.last_name} -- {self.last_name}"

