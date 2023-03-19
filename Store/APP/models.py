from django.db import models
import json

class Category(models.Model):
    category_name = models.CharField(max_length=128, default='Имя не присвоено')
    category_picture = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'\
        
    def create_categories(self):
        new_clothes = Category.objects.create(
            category_name='Новая одежда',
            category_picture='images/Новая одежда.jpg'
        )
        used_clothes = Category.objects.create(
            category_name='БУ одежда',
            category_picture='images/БУ одежда.jpg'
        )
        
    
        
class Product(models.Model):
    __max__id = 1
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование товара',max_length=50)
    brand = models.CharField(verbose_name='Бренд', max_length=50)
    color = models.CharField(verbose_name='Цвет', max_length=50)
    size = models.CharField(verbose_name='Размер', max_length=20)
    price = models.IntegerField(verbose_name='Цена')

    def __init__(self, category:str, name:str, brand:str, color:str, size:str, price:int):
        self.id = Product.__max__id
        self.category = category
        self.name = name
        self.brand = brand
        self.color = color
        self.size = size
        self.price = price
        Product.__max__id +=1

    def __str__(self):
        return(
            f'ID: {self.id}\n'
            +f'Наименование товара: {self.name}\n'
            +f'Торговая марка: {self.brand}\n'
            +f'Категория товара: {self.category}\n'
            +f'Цвет: {self.color}\n'
            +f'Размер: {self.size}\n'
            +f'Цена товара: {self.price}'
            )