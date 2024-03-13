from django.contrib import admin
from .models import Category, Subcategory, Service, ServiceImage, Employee, Vacancy, JobApplication, ContactInfo, ContactPhoneNumber, ContactApplication, SocialMedia

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImageInline]
    list_display = ['name', 'subcategory', 'get_category', 'description']

    def get_category(self, obj):
        return obj.subcategory.category.name
    get_category.short_description = 'Category'

class ContactPhoneNumberInline(admin.TabularInline):
    model = ContactPhoneNumber
    extra = 1

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    inlines = [ContactPhoneNumberInline]
    list_display = ['address', 'email', 'get_main_number']

    def get_main_number(self, obj):
        return obj.main_number
    get_main_number.short_description = 'Main Number'

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Employee)
admin.site.register(Vacancy)
admin.site.register(JobApplication)
admin.site.register(ContactApplication)
admin.site.register(SocialMedia)
