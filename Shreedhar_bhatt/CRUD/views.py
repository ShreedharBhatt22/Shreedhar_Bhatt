# contacts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'response.html', {'contacts': contacts})

def new_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'Latest front.html', {'form': form})

def contact_details(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'details.html', {'contact': contact})

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_details', contact_id=contact.id)
    else:
        form = ContactForm(instance=contact)

    return render(request, 'Update page.html', {'form': form, 'contact': contact})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    if request.method == 'POST':
        contact.delete()
        return redirect('home')

    return render(request, 'delete page.html', {'contact': contact})