from django.db import models

# Create your models here.
class Product(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stock = models.IntegerField(verbose_name='재고')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self): #상품이름을 리턴받는다.
        return self.name
        
    class Meta:
        db_table = 'store_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'