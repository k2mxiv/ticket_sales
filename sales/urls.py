from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:product_id>/', views.detail, name = 'detail'),
    path('create/', views.product_create, name = 'product_create'),
    path('sales/modify/<int:product_id>/', views.product_modify, name = 'product_modify'),
    path('sales/delete/<int:product_id>/', views.product_delete, name = "product_delete"),
    path('sales/sales_create/<int:product_id>/', views.sales_create, name = 'sales_create'),
    path('sales/full_list/', views.full_history, name = 'full_list'),
    path('sales/delete_list/', views.delete_history, name = 'delete_list'),
    path('sales/live_list/', views.live_history, name = 'live_list'),
    path('sales/media/<img_str>', views.img_dir, name = 'media'),
]
