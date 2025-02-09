from django.urls import path

from . import views

urlpatterns = [
    path("goods", views.goods_list),
    path("goods_detail/<int:pk>", views.goods_detail)
]