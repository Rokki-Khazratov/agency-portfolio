from rest_framework import generics
from .models import Category, Subcategory, Service, Employee, Vacancy, JobApplication, ContactInfo, ContactApplication, SocialMedia
from .serializers import CategorySerializer, ServiceDetailSerializer, SubcategorySerializer, ServiceSerializer, EmployeeSerializer, VacancySerializer, JobApplicationSerializer, ContactInfoSerializer, ContactApplicationSerializer, SocialMediaSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        self_made = self.request.query_params.get('self_made', None)
            
        if self_made:
            queryset = queryset.filter(self_made=self_made)

        return queryset
    

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ServiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer





class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class VacancyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class JobApplicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class JobApplicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer


class ContactInfoListCreateAPIView(generics.ListCreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class ContactInfoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class ContactApplicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = ContactApplication.objects.all()
    serializer_class = ContactApplicationSerializer

class ContactApplicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactApplication.objects.all()
    serializer_class = ContactApplicationSerializer

class SocialMediaListCreateAPIView(generics.ListCreateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class SocialMediaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
