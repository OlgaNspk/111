from django.http import FileResponse, Http404, HttpResponse, HttpResponseRedirect, JsonResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.template.loader import get_template
from .models import Product, Category

products = Product.objects.all()


def products_view(request):
    if request.method == 'GET':
        category = request.GET.get('category', None)
        products = Product.objects.all()
        if category:
            products = products.filter(category_name=category)
        return HttpResponse(',\n\n'.join(str(product) for product in products))
    elif request.method == 'POST':
        body = json.loads(request.body)
        product = Product(
            name=body['name'],
            category_name=body['category'],
            brand=body['brand'],
            color=body['color'],
            size=body['size'],
            price=body['price']
        )
        product.save()
        return HttpResponse(str(product), status=200)
    else:
        return HttpResponse(status=405)


def product_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        if product.name == '':
            return HttpResponseRedirect(reverse('products'))
        return HttpResponse(str(product))
    else:
        return HttpResponse(status=405)

list_of_dict_products = [product.__dict__ for product in Product.objects.all()]



categories_img = {
    'Новая одежда': 'APP\images\Новая одежда.jpg',
    'БУ одежда': 'APP\images\БУ одежда.jpg'
}

def category_image_view(request, name):
    try:
        category = Category.objects.get(name=name)
    except Category.DoesNotExist:
        raise Http404()
    return FileResponse(open(category.image.path, 'rb'), as_attachment=True)
