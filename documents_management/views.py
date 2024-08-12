from django.shortcuts import render, redirect, get_object_or_404
from .models import Documents
from .forms import DocumentForm, DocumentCreateForm
from django.contrib import messages
# Create your views here.

def home(request):
    title='All The Documents'
    queryset= Documents.objects.all()
    context = {'title': title,
                                'queryset': queryset
               }
    return render(request, 'home.html', context)

def add_document(request):
    form = DocumentCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Added')
        return redirect('/')
    context={
        'form':form,
        'title':'Add a Document'
    }
    return render(request, "add_document.html", context)

def delete_items(request, pk):
    queryset = Documents.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('/')
    return render(request, 'delete_items.html', {'queryset': queryset})


def display_document(request, pk):
    document = get_object_or_404(Documents, pk=pk)
    return render(request, 'display_document.html', {'document': document})