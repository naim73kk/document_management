from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class Documents(models.Model):
    category= models.CharField(max_length=50, blank=True, null = False)
    document_name = models.CharField(max_length=50, blank=True, null= False)
    pdf_document = models.FileField(upload_to='documents', validators=[FileExtensionValidator(['pdf'])])
    # def __str__(self):
    #     return self.category+ '   ' + self.document_name

