from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),

    path('services/', ServiceListCreateAPIView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceRetrieveUpdateDestroyAPIView.as_view(), name='service-detail'),

    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(), name='employee-detail'),

    path('vacancies/', VacancyListCreateAPIView.as_view(), name='vacancy-list'),
    path('vacancies/<int:pk>/', VacancyRetrieveUpdateDestroyAPIView.as_view(), name='vacancy-detail'),

    path('jobapplications/', JobApplicationListCreateAPIView.as_view(), name='jobapplication-list'),
    path('jobapplications/<int:pk>/', JobApplicationRetrieveUpdateDestroyAPIView.as_view(), name='jobapplication-detail'),

    path('contactinfo/', ContactInfoListCreateAPIView.as_view(), name='contactinfo-list'),
    path('contactinfo/<int:pk>/', ContactInfoRetrieveUpdateDestroyAPIView.as_view(), name='contactinfo-detail'),

    path('contactapplications/', ContactApplicationListCreateAPIView.as_view(), name='contactapplication-list'),
    path('contactapplications/<int:pk>/', ContactApplicationRetrieveUpdateDestroyAPIView.as_view(), name='contactapplication-detail'),

    path('socialmedias/', SocialMediaListCreateAPIView.as_view(), name='socialmedia-list'),
    path('socialmedias/<int:pk>/', SocialMediaRetrieveUpdateDestroyAPIView.as_view(), name='socialmedia-detail'),
]
