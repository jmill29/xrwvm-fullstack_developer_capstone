from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
  list_display = ('name', 'car_type', 'release_year', 'mileage')
  list_filter = ['make', 'release_year', 'car_type']
  search_fields = ['dealer_id', 'name']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
  inlines = [CarModelInline]
  list_display = ('name', 'hq_state', 'hq_city')
  list_filter = ['hq_state', 'hq_city']
  search_fields = ['name']

# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)