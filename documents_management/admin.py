from django.contrib import admin
from .models import Documents
from .forms import DocumentForm  # Corrected form import

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['category', 'document_name','pdf_document']  # Ensure field names are correct
    form = DocumentForm  # Use the correct form class
    list_filter = ['category']
    search_fields = ['category', 'document_name']

admin.site.register(Documents, DocumentAdmin)
