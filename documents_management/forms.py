from django import forms
from .models import Documents


class DocumentCreateForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['category', 'document_name']

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')

        # for instance in Stock.objects.all():
        #     if instance.category == category :
        #         raise forms.ValidationError(str(category) + ' is already created')
        return category

    def clean_document_name(self):
        document_name = self.cleaned_data.get('document_name')
        if not document_name:
            raise forms.ValidationError('This field is required')
        return document_name


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['category', 'document_name','pdf_document']  # Ensure the field names are correct
