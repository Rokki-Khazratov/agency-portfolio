from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='service_images/')




class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='employee_images/')

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    position = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='vacancy_images/',blank=True,null=True)

    def __str__(self):
        return self.position

class JobApplication(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name



class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField()
    main_number = models.CharField(max_length=20)

class ContactPhoneNumber(models.Model):
    contact = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True,null=True)
    number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.number}"
    
class ContactApplication(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)
    message = models.TextField(blank=True,null=True)

class SocialMedia(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()