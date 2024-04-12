from rest_framework import generics
from django.http import Http404
from .models import Category, Subcategory, Service, Employee, Vacancy, JobApplication, ContactInfo, ContactApplication, SocialMedia
from .serializers import CategorySerializer, ServiceDetailSerializer, SubcategorySerializer, ServiceSerializer, EmployeeSerializer, VacancySerializer, JobApplicationSerializer, ContactInfoSerializer, ContactApplicationSerializer, SocialMediaSerializer
from .permissions import IsAdminOr404

class BasePermissionAPIView(generics.GenericAPIView):
    permission_classes = [IsAdminOr404]

    def list(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise Http404("You are not authorized to access this resource.")
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise Http404("You are not authorized to access this resource.")
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise Http404("You are not authorized to access this resource.")
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise Http404("You are not authorized to access this resource.")
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise Http404("You are not authorized to access this resource.")
        return super().destroy(request, *args, **kwargs)


# class CategoryListCreateAPIView(BasePermissionAPIView, generics.ListCreateAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()

# class CategoryRetrieveUpdateDestroyAPIView(BasePermissionAPIView, generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()

# class ServiceListCreateAPIView(BasePermissionAPIView, generics.ListCreateAPIView):
#     serializer_class = ServiceSerializer
#     queryset = Service.objects.all()

# class ServiceRetrieveUpdateDestroyAPIView(BasePermissionAPIView, generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ServiceDetailSerializer
#     queryset = Service.objects.all()

# class EmployeeListCreateAPIView(BasePermissionAPIView, generics.ListCreateAPIView):
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()

# class EmployeeRetrieveUpdateDestroyAPIView(BasePermissionAPIView, generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = EmployeeSerializer
#     queryset = Employee.objects.all()

# class VacancyListCreateAPIView(BasePermissionAPIView, generics.ListCreateAPIView):
#     serializer_class = VacancySerializer
#     queryset = Vacancy.objects.all()

# class VacancyRetrieveUpdateDestroyAPIView(BasePermissionAPIView, generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = VacancySerializer
#     queryset = Vacancy.objects.all()

# class JobApplicationListCreateAPIView(BasePermissionAPIView, generics.ListCreateAPIView):
#     serializer_class = JobApplicationSerializer
#     queryset = JobApplication.objects.all()

# class JobApplicationRetrieveUpdateDestroyAPIView(BasePermissionAPIView, generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = JobApplicationSerializer
#     queryset = JobApplication.objects.all()

# class ContactInfoListCreateAPIView(BasePermissionAPIView, generics.ListCreateAPIView):
#     serializer_class = ContactInfoSerializer
#     queryset = ContactInfo.objects.all()

# class ContactInfoRetrieveUpdateDestroyAPIView(BasePermissionAPIView, generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ContactInfoSerializer
#     queryset = ContactInfo.objects.all()

# class ContactApplicationListCreateAPIView(BasePermissionAPIView, generics.ListCreateAPIView):
#     serializer_class = ContactApplicationSerializer
#     queryset = ContactApplication.objects.all()

# class ContactApplicationRetrieveUpdateDestroyAPIView(BasePermissionAPIView, generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ContactApplicationSerializer
#     queryset = ContactApplication.objects.all()

# class SocialMediaListCreateAPIView(BasePermissionAPIView, generics.ListCreateAPIView):
#     serializer_class = SocialMediaSerializer
#     queryset = SocialMedia.objects.all()

# class SocialMediaRetrieveUpdateDestroyAPIView(BasePermissionAPIView, generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = SocialMediaSerializer
#     queryset = SocialMedia.objects.all()






class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ServiceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        subcategory_id = self.request.query_params.get('subcategory_id')
        name = self.request.query_params.get('name')

        queryset = Service.objects.all()

        if subcategory_id:
            # Filter services by subcategory_id if provided
            queryset = queryset.filter(subcategory_id=subcategory_id)

        if name:
            # Filter services by name if name query parameter is provided
            queryset = queryset.filter(name__icontains=name)

        return queryset


class ServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceDetailSerializer
    queryset = Service.objects.all()

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class VacancyListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

class VacancyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

class JobApplicationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = JobApplicationSerializer
    queryset = JobApplication.objects.all()

class JobApplicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobApplicationSerializer
    queryset = JobApplication.objects.all()

class ContactInfoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ContactInfoSerializer
    queryset = ContactInfo.objects.all()

class ContactInfoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactInfoSerializer
    queryset = ContactInfo.objects.all()

class ContactApplicationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ContactApplicationSerializer
    queryset = ContactApplication.objects.all()

class ContactApplicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactApplicationSerializer
    queryset = ContactApplication.objects.all()

class SocialMediaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()

class SocialMediaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()
