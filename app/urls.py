from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('demand/', demand, name="demand"),
    path('geography/', geography, name="geography"),
    path('skills/', skills, name="skills"),
    path('recentv/', recentv, name="recentv"),
]