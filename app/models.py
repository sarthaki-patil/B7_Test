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


class Company(models.Model):
    name = models.CharField(max_length = 255)
    owner_name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    email = models.EmailField()
    num_of_emp = models.IntegerField()
  

    class Meta:
        db_table = "company"

    def __str__(self):
        return f"{self.name} -- {self.owner_name}"