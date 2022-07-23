from django.urls import path
from delivery import views

urlpatterns = [
    path('orders/', views.order_list, name="order_list")
    # path('timeinput/', views.time_input, name="timeinput"),
]