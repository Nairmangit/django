from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.Add, name='add'),
    path('complete/<comp_id>', views.Complete, name='complete'),
    path('dcomplete/<comp_id>', views.dComplete, name='dcomplete'),
    path('deletecomplete', views.deleteComp, name='deletecomplete')
]
