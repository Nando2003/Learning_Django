from django.contrib import admin
from django.urls import path, include
from recipes.views import home_view, sobre_view, contato_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),  # HOME
    path('sobre/', sobre_view),  # SOBRE
    path('contato/', contato_view)   # CONTATO

]
