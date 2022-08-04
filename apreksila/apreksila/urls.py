
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guide/', views.guide),
    path('prediksi/', include('prediksi_usia.urls')),
    path('results/', include('prediksi_usia.urls')),
    path('', views.index),
    path('index', views.index),
]

admin.site.site_header = "Apreksila Admin Page"
admin.site.site_title = "Admin Page"
admin.site.index_title = "Welcome to Admin Page"