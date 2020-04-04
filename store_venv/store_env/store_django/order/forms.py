from django import forms
from .models import Order
from product.models import Product
from stuser.models import Stuser

class RegisterForm(forms.Form):
    def __init__(self,request, *args, **kwangs):     # form안에서 request를 전달해줘야한다. init함수(생성자)를 만들면서 request를 form에전달할 수 있게 해주고 다음에 formview와 form을 생성할 때 request를 전달할수있게
        super().__init__(*args, **kwangs)
        self.request = request
    
    quantity = forms.IntegerField(
        error_messages={
            'required' : '수량을 입력해주세요'
        },  label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required: 상품설명을 입력해주세요'
        }, label='상품설명', widget = forms.HiddenInput
    )
    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        stuser = self.request.session.get('user') #이메일을 가지고온다

        if quantity and product and stuser:
            order = Order(
                quantity = quantity,
                product = Product.objects.get(pk=product),
                stuser=Stuser.objects.get(email=stuser)

            )   
            order.save()    
        else:
            self.add_error('quantity', '값이 없습니다')
            self.add_error('product', '값이 없습니다')
