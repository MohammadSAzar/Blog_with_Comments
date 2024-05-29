from django.shortcuts import render, redirect
from .models import City, District
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
    cities = City.objects.filter(province_id=province_id).all()
    return render(request, 'rs/city_dropdown_list_options.html', {'cities': cities})

def load_districts(request):
    city_id = request.GET.get('city')
    districts = District.objects.filter(city_id=city_id).all()
    return render(request, 'rs/district_dropdown_list_options.html', {'districts': districts})
