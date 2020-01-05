from django.shortcuts import render
from .forms import ContactForm
from .local_settings import email_func
from django import forms
from django.core.mail import send_mail
import datetime

def page_contact(request):

    if request.method == 'POST':
        to = email_func.EMAIL_HOST_USER
        subject = 'Заявка',
        message = 'Прислал {} {} {} . Телефон: {}. Email: {}. Дополнительная информация : {}. Дата: {} '.format(
            request.POST['first_name'], 
            request.POST['last_name'], 
            request.POST['second_name'], 
            request.POST['contact_phone'], 
            request.POST['contact_email'], 
            request.POST['comment'],
            str(datetime.datetime.now()))
        email_func.EMAIL_HOST_USER
        send_mail(subject, message, [to], [to])
        sent = True
    return render(request, 'bs/contact.html')

def work(request):
    return render(request, 'bs/photo.html')

"""def page_contact(request):
    sent = False
    mailfrom = email_func.EMAIL_HOST_USER
    mailto = [email_func.EMAIL_HOST_USER]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Autister - Новое письмо от {}'.format(cd['name'])
            message = 'Прислал {}. Пишет: {}'.format(cd['email'], cd['message'])
            email_func.send_mail(subject, message, mailfrom, mailto)
            sent = True
    else:
        form = ContactForm()
    return render(request, 'bs/contact.html')"""

