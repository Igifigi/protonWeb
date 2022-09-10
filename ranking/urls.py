from django.urls import path
from django.views.decorators.cache import never_cache

from .views import *

urlpatterns = [
    path('', test)
]
