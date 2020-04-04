from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm

# Create your views here.
class OrderCreate(FormView):
    form_class = RegisterForm    
    success_url = '/product/'

    def get_form_kwargs(self, **kwargs): # form을 생성할떄 어떤 인자값을 전달해서 만들건지 
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw