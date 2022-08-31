from django.shortcuts import render, redirect

from .forms import CustomForm
from .models import Document


def home(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gen')

    form = CustomForm()

    return render(request, 'docs/home.html', {'form': form})


def generated(request):
    doc = Document.objects.order_by('-pk').first()
    return render(request, 'docs/generated_doc.html', {"doc": doc})
