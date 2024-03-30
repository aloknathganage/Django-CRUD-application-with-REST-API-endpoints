from . import views
from django.urls import path
from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import createclass, deleteclass, readclass, updateclass
from .views import *



urlpatterns = [
    path("",views.homeo,name='homeo'),
    # path("add",views.home,name='home'),
    # path("view/<int:task_id>",views.show,name='show'),
    path('api/add/', createclass.as_view(), name='createclass'),
    path('api/view/<int:task_id>/', readclass.as_view(), name='modelapiview'),
    path('api/view/', getall.as_view(), name='get_all_api'),
    path('api/delete/<int:task_id>/',deleteclass.as_view(),name='delete_task'),
    path('api/update/<int:task_id>/',updateclass.as_view(),name='update_task'),

]

