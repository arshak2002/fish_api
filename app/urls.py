
from django.urls import path
from .views import*

urlpatterns = [
    path('',Home.as_view()),
    path('single/<int:id>/',Single.as_view()),
    path('order/<int:id>',OrderFish.as_view()),
    path('myorder',MyOrder.as_view()),
    path('search',Search.as_view()),


    path('AdminHome',AdminHome.as_view()),
    path('edit/<int:id>',AdminEdit.as_view()),
    path('adminOrderView/',AdminViewOrder.as_view()),

]