from django.urls import include, path
from . import views
from rest_framework import routers #specific to rest_framework

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)

urlpatterns = [
    path('', include(router.urls))
    
]
