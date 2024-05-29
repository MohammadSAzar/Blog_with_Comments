from django.contrib import admin
from .models import RealEstate, Province, City, District


@admin.register(RealEstate)
class RealEstateAdmin(admin.ModelAdmin):
	list_display = ('province', 'city', 'district', 'price', 'room', 'area', 'year', 'floor', 'parking', 'elevator', 'warehouse', 'document', 'description', 'status', 'datetime_created')
	ordering = ('-datetime_created',)
# prepopulated_fields = {'slug': ('title',)}

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	list_display = ('name', 'province')

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
	list_display = ('name', 'city')
