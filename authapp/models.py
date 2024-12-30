from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=12)
    description = models.TextField()

    def __str__(self):
        return self.email

class Enrollment(models.Model):
    FullName = models.CharField(max_length=255)  # Adjusted field name to start with uppercase (convention)
    Email = models.EmailField()
    Gender = models.CharField(max_length=25)
    PhoneNumber = models.CharField(max_length=12)
    DOB = models.CharField(max_length=50)  # Consider using DateField or DateTimeField for dates
    SelectMembershipplan = models.CharField(max_length=200)
    SelectTrainer = models.CharField(max_length=55)
    Reference = models.CharField(max_length=55)
    Address = models.TextField()
    paymentStatus = models.CharField(max_length=55, blank=True, null=True)
    Price = models.IntegerField(blank=True, null=True)  # Removed unnecessary max_length
    DueDate = models.DateTimeField(blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.FullName

class Trainer(models.Model):
    name = models.CharField(max_length=55)
    gender = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    salary = models.IntegerField()  # Removed unnecessary max_length
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    plan = models.CharField(max_length=185)
    price = models.IntegerField()

    def __str__(self):
        return self.plan

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='gallery')
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Attendance(models.Model):
    Selectdate = models.DateTimeField(auto_now_add=True)
    phonenumber = models.CharField(max_length=15)
    Login = models.CharField(max_length=200)
    Logout = models.CharField(max_length=200)
    SelectWorkout = models.CharField(max_length=200)
    TrainedBy = models.CharField(max_length=200)

    def __str__(self):
        return f"Attendance - {self.id}"  # Adjusted to return a meaningful string representation
