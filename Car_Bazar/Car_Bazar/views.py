from django.shortcuts import render, redirect
from car.models import Add_Car
from brand.models import Brand
def home(request, brand_slug=None):
    datas = Add_Car.objects.all()
    brands = Brand.objects.all()
    if brand_slug is not None:
        car_brand = Brand.objects.get(slug=brand_slug)
        datas = Add_Car.objects.filter(car_brand=car_brand)
    return render(request, 'home.html', {'datas': datas, 'brands': brands})