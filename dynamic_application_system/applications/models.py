from django.db import models

# Panagiotis Bellias
class SamplePersonModel(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return f"with full name {self.full_name}"

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
    job = models.TextField(default='unemployeed')

    def __str__(self):
        return f"Citizen {super().__str__()}, {self.job}"

class PersonnelDepartment(models.Model):
    address = models.TextField()

    def __str__(self):
        return f"Personnel department with address {self.address}"

class Application(models.Model):
    id = models.AutoField(primary_key=True)
    pub_date = models.DateTimeField('date published')
    headline = models.CharField(max_length=200)
    #content = models.CharField() # dynamic 1
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)

    def __str__(self):
        return f"Application with headline {self.headline}"

# dynamic 3
class ApplicationContent(models.Model):
    application = models.ForeignKey(Application)
    content = models.CharField()