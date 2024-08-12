# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from documents_management import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_document/', views.add_document, name='add_document'),
    path('display_document/<str:pk>/', views.display_document, name='display_document'),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    path('admin/', admin.site.urls),
]

# This line is critical to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
