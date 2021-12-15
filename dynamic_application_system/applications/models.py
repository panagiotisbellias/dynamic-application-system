from django.db import models

# Panagiotis Bellias
class SamplePersonModel(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Manager(SamplePersonModel):
    def __str__(self):
        return f"Manager {super().__str__()}"

class Carrier(SamplePersonModel):
    job_object = models.TextField()

    def __str__(self):
        return f"Carrier {super().__str__()} with job object {self.job_object}"

class SuperVisor(SamplePersonModel):
    def __str__(self):
        return f"Supervisor {super().__str__()}"

class Citizen(SamplePersonModel):
    def __str__(self):
        return f"Citizen {super().__str__()}"

class PersonnelDepartment(models.Model):
    address = models.TextField()

    def __str__(self):
        return f"Personnel department {super().__str__()} with address {self.address}"

class Application(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)

    def __str__(self):
        return f"Application with headline {self.headline}"