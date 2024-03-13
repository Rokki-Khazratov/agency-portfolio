from rest_framework import serializers
from .models import Category, Subcategory, Service, ServiceImage, Employee, Vacancy, JobApplication, ContactInfo, ContactPhoneNumber, ContactApplication, SocialMedia


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name', 'description']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'subcategories']

    def get_subcategories(self, obj):
        subcategories = Subcategory.objects.filter(category=obj)
        return SubcategorySerializer(subcategories, many=True).data




class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ['id', 'service', 'image']

class ServiceSerializer(serializers.ModelSerializer):
    subcategory = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ['id', 'subcategory', 'name', 'description', 'images']

    def get_subcategory(self, obj):
        return obj.subcategory.name if obj.subcategory else None

    def get_images(self, obj):
        images = obj.images.all()
        request = self.context.get('request')
        return [request.build_absolute_uri(image.image.url) for image in images]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'position', 'image']

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'position', 'description', 'image']

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['id', 'vacancy', 'name', 'phone_number', 'resume']

class ContactPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPhoneNumber
        fields = ['id', 'contact', 'name', 'number']

class ContactInfoSerializer(serializers.ModelSerializer):
    phone_numbers = ContactPhoneNumberSerializer(many=True, read_only=True)
    class Meta:
        model = ContactInfo
        fields = ['id', 'address', 'email', 'main_number', 'phone_numbers']

class ContactApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactApplication
        fields = ['id', 'name', 'phone_number', 'email', 'message']

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['id', 'platform', 'url']
