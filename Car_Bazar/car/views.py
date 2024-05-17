from django.shortcuts import render,redirect,get_object_or_404
from . forms import UserRegistrationForm, EditUserForm
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Add_Car
from comment.forms import CommentForm
# Create your views here.

class UserRegistration(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "user_registration.html"
    success_url = reverse_lazy("user_login")
    
class UserLogin(LoginView):
    template_name = "user_registration.html"
    
    def get_success_url(self):
        return reverse_lazy("profile")
    
    def form_valid(self, form):
        messages.success(self.request, "User Logged in successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, "Invalid Information")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"]="Login"
        return context
    

class EditUserProfile(UpdateView):
    model = User
    form_class = EditUserForm
    template_name = "edit_profile.html"
    success_url = reverse_lazy("profile")
    pk_url_kwarg = 'pk'
    

def UserProfile(request):
    cars = Add_Car.objects.filter(buyer=request.user)
    return render(request,"profile.html", {"cars": cars})

def user_logout(request):
    logout(request)
    return redirect('home')

def car_detail(request,pk):
    car = get_object_or_404(Add_Car, pk=pk)
    comments = car.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
    else:
        comment_form = CommentForm()
        
    context = {
        'car': car,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'car_detail.html', context)


def buy_car(request, pk):
    car = get_object_or_404(Add_Car, pk=pk)
    car.car_quantity -= 1
    car.buyer.add(request.user)
    car.save()
    return redirect("profile")