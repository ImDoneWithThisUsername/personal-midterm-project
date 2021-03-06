from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('account/', views.accountSettings, name="account"),

    path('create_order/<str:pk>/', view=views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', view=views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', view=views.deleteOrder, name="delete_order"),

]
