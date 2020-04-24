from django.shortcuts import render

from django.http.response import HttpResponse, JsonResponse
from api.models import Product, Category

def product_list(request):
    try:
        products = Product.objects.all()
        products_json = [product.to_json() for product in products]
        return JsonResponse(products_json, safe=False)
    except:
        return JsonResponse({ "message": "no products" })


def product_detailed(request, id):
    try:
        product = Product.objects.get(id = id)
        product_json = product.to_json()
        return JsonResponse(product_json, safe=False)
    except:
        return JsonResponse({ "message": "no product" })

def category_list(request):
    try:
        categories = Category.objects.all()
        categories_json = [category.to_json() for category in categories]
        return JsonResponse(categories_json, safe=False)
    except:
        return JsonResponse({ "message": "no categories" })


def category_detailed(request, id):
    try:
        category = Category.objects.get(id = id)
        category_json = category.to_json()
        return JsonResponse(category_json, safe=False)
    except:
        return JsonResponse({ "message": "no category" })

def category_products(request, id):
    try:
        category = Category.objects.get(id = id)
        products = category.product_set.all()
        products_json = [product.to_json() for product in products]
        return JsonResponse(products_json, safe=False)
    except:
        return JsonResponse({ "message": "no products" })