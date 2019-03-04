# -*- coding: utf-8 -*-

from smtplib import SMTPException

from django import forms
from django.core.mail import EmailMessage
from .models import Contact


class ContactForm(forms.ModelForm):
    OPTION = (
        ("CELPIP","CELPIP"),
        ("IELTS","IELTS"),
        ("PTE","PTE"),
        ("ALL","ALL"),
        )

    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'placeholder': "Name *", 'required': ""}),
    )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'placeholder': "Phone Number *", 'required': ""}),
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'placeholder': "Subject *", 'required': ""}),
    )
    products = forms.CharField(widget=forms.Select(choices=OPTION, attrs={'class':'form-control','tabindex':1}))

    class Meta:
        model = Contact
        fields = ('name', 'phone', 'subject', 'message',)

    def clean_subject(self):
        subject = ''.join(self.cleaned_data['subject'].splitlines())
        return subject

    def send_email(self):
        email = EmailMessage(
            self.cleaned_data['subject'],
            self.cleaned_data['message'],
            '',
            ['admin@example.com'],
            reply_to=['{name} <{phone}>'.format(**self.cleaned_data)],
        )
        try:
            email.send()
            return True
        except SMTPException:
            return False
