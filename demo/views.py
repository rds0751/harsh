# -*- coding: utf-8 -*-

from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib import messages

from .forms import ContactForm
from .models import Contact


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'demo/demo.html'

    def get_success_url(self):
        return reverse('demo:demo')

    def form_valid(self, form):
        model = Contact()

        model.name = form.cleaned_data['name']
        model.phone = form.cleaned_data['phone']
        model.email = form.cleaned_data['email']
        model.products = form.cleaned_data['products']
        model.save()
        if form.send_email():
            messages.info(self.request, 'Thank you for your message. We will be in touch shortly.')
        else:
            messages.error(self.request, "We couldn't send your message. Please try again later.")
        return super(ContactView, self).form_valid(form)

from django.shortcuts import render

def contacts(request):
    items = Contact.objects.all()
    return render(request, 'demo/demos.html', locals())