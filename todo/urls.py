from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo', views.TodoView)

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.Add, name='add'),
    path('complete/<comp_id>', views.Complete, name='complete'),
    path('dcomplete/<comp_id>', views.dComplete, name='dcomplete'),
    path('deletecomplete', views.deleteComp, name='deletecomplete'),
    path('apirest_', include(router.urls))
]
