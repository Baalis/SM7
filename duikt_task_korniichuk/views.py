from django.http import HttpResponse
from django.shortcuts import render
from .models import cars_brand, cars_info

def install(request):
    output = []

    demo_brands = [
        {"BRAND_NAME": "Toyota", "BRAND_COUNTRY": "Japan", "BRAND_RATING": 9},
        {"BRAND_NAME": "Ford", "BRAND_COUNTRY": "USA", "BRAND_RATING": 8},
        {"BRAND_NAME": "BMW", "BRAND_COUNTRY": "Germany", "BRAND_RATING": 9},
    ]

    demo_cars = [
        {"CAR_NAME": "Corolla", "CAR_MODEL": "2023", "CAR_PRICE": 20000, "CAR_BRAND": "Toyota"},
        {"CAR_NAME": "Mustang", "CAR_MODEL": "2022", "CAR_PRICE": 35000, "CAR_BRAND": "Ford"},
        {"CAR_NAME": "X5", "CAR_MODEL": "2023", "CAR_PRICE": 60000, "CAR_BRAND": "BMW"},
    ]

    # Додаємо бренди
    for b in demo_brands:
        obj, created = cars_brand.objects.get_or_create(
            BRAND_NAME=b["BRAND_NAME"],
            defaults={
                "BRAND_COUNTRY": b["BRAND_COUNTRY"],
                "BRAND_RATING": b["BRAND_RATING"]
            }
        )
        output.append(f"{'Створено' if created else 'Пропущено (вже існує)'} бренд: {obj.BRAND_NAME}")

    # Додаємо машини
    for c in demo_cars:
        brand = cars_brand.objects.get(BRAND_NAME=c["CAR_BRAND"])
        obj, created = cars_info.objects.get_or_create(
            CAR_NAME=c["CAR_NAME"],
            CAR_MODEL=c["CAR_MODEL"],
            defaults={
                "CAR_PRICE": c["CAR_PRICE"],
                "CAR_BRAND": brand
            }
        )
        output.append(f"{'Створено' if created else 'Пропущено (вже існує)'} авто: {brand.BRAND_NAME} {c['CAR_NAME']}")

    return HttpResponse("<br>".join(output))


def show_page(request):
    cars = cars_info.objects.all()
    return render(request, "template.html", {"cars": cars})
