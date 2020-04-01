from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from order.forms import RegisterForm as OrderForm
# from django.views.generic import FormView
# from .forms import RegisterForm
# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'

# class ProductCreate(FormView):
#     model = Product
#     template_name = 'product.html'
#     context_object_name = 'product_list'

    # template_name = 'register_product.html'
    # form_class = RegisterForm
    # success_url = '/product'

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all() # 어떤 모델을 지정하는게 아니라 쿼리셋을 지정
    context_object_name = 'product'
    
    def get_context_data(self, **kwangs): # detailform 에 전달되는 게 필요, 내가 원하는 데이터를 집어넣을 수 있게
        context = super().get_context_data(**kwangs) # 먼저 디테일 view가 원하는 것을 만든 다음
        context['form'] = OrderForm()
        return context
