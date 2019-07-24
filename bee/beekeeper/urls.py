from django.urls import path
from .views import beet
# from .views import index
urlpatterns = {
    path('', beet),
#    path('', index),
}

