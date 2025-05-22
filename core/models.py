from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(db_index=True)
    description=models.CharField()

class ProductImage(models.Model):
    image=models.ImageField(upload_to='products/')
    alt_text=models.CharField(max_length=200)
    img_height=models.PositiveIntegerField()
    img_width=models.PositiveIntegerField()

class Product(models.Model):
    name=models.CharField(max_length=200,db_index=True)
    description=models.TextField()
    available=models.BooleanField(db_index=True)
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    image=models.OneToOneField(ProductImage,related_name='product',on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=5,decimal_places=2)


