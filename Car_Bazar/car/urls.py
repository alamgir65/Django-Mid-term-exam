from django.urls import path
from . import views

urlpatterns = [
    path('user_register/', views.UserRegistration.as_view(), name="user_registration"),
    path('user_login/', views.UserLogin.as_view(), name="user_login"),
    path('user_logout/', views.user_logout , name="user_logout"),
    path('user_profile/', views.UserProfile, name="profile"),
    # path('change_password/', views.ChangePassword.as_view(), name="change_password"),
    path('car_detail/<int:pk>/', views.car_detail, name="car_detail"),
    path('buy_car/<int:pk>/', views.buy_car, name="buy_car"),
    path('edit/<int:pk>/', views.EditUserProfile.as_view(), name="edit_profile"),
]