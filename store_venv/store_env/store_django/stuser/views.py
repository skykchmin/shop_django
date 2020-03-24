from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
# Create your views here.

def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')}) #세션에 email 전달


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form): #로그인이 정상적으로 수행되었을때
        self.request.session['user'] = form.email #로그인한 사용자 정보를 세션에 저장
        
        return super().form_valid(form)
