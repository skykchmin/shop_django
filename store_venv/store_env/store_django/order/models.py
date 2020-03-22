from django.db import models

# Create your models here.
class Order(models.Model):
    stuser = models.ForeignKey('stuser.Stuser', on_delete=models.CASCADE, verbose_name='사용자') # on_delete 사용자가 삭제되었을 떄 order는 어떻게 할 것인가
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return str(self.stuser)+ ' ' + str(self.product)

    class Meta:
        db_table = 'store_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'