from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page),
    path('demand/', demand_page),
    path('geography/', geography_page),
    path('skills/', skills_page),
    path('recentv/', recentv_page),
]