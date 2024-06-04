from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import City, District, RealEstate
from .forms import RealEstateForm

def real_estate_create(request):
    if request.method == 'POST':
        form = RealEstateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or any desired URL
    else:
        form = RealEstateForm()
    return render(request, 'rs/create_real_estate.html', {'form': form})

def load_cities(request):
    province_id = request.GET.get('province')
    cities = City.objects.filter(province_id=province_id).order_by('name')
    city_choices = [(city.id, city.name) for city in cities]
    return JsonResponse({'cities': city_choices})

def load_districts(request):
    city_id = request.GET.get('city')
    districts = District.objects.filter(city_id=city_id).order_by('name')
    district_choices = [(district.id, district.name) for district in districts]
    return JsonResponse({'districts': district_choices})

