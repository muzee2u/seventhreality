from django.core.mail import send_mail, EmailMessage
from BRL_Portfolio.settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from RD_Projects.models import *
from staff.models import *
from publications.models import *
from blogs.models import *
from datetime import date
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string


def index(request):
    projects = Project.objects.all()[:6]
    papers = ResearchPaper.objects.all()[:3]
    blogs = Blog.objects.all()[:3]
    employees = Employee.objects.all()
    dict_obj = {'projects': projects, 'papers': papers, 'blogs': blogs, 'employees': employees}
    return render(request, 'index.html', dict_obj)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        today = date.today()
        today_date = today.strftime("%d %B, %Y")
        print(today_date)
        try:
            # send_mail(subject, "Thank you for your contact", EMAIL_HOST_USER, [email], fail_silently=False)
            # send_mail(subject, message, email, [EMAIL_HOST_USER], fail_silently=False, reply_to=email)

            c = ({'test': today_date})
            msg_html = render_to_string('email.html', c, request=request)

            # # I used EmailMultiAlternatives because I wanted to send both text and html
            # emailMessage = EmailMultiAlternatives(subject=subject, body=message, from_email=EMAIL_HOST_USER,
            #                                       to=[email, ], reply_to=[EMAIL_HOST_USER, ])
            # emailMessage.attach_alternative(msg_html, "text/html")
            # emailMessage.send(fail_silently=False)

            send_mail(
                'no-reply',
                message,
                EMAIL_HOST_USER,
                [email],
                html_message=msg_html,
            )

            # I used EmailMultiAlternatives because I wanted to send both text and html
            emailMessage = EmailMultiAlternatives(subject=subject, body=message, from_email=EMAIL_HOST_USER,
                                                  to=[EMAIL_HOST_USER, ], reply_to=[email, ])
            emailMessage.attach_alternative(msg_html, "text/html")
            emailMessage.send(fail_silently=False)

        except Exception as e:
            return redirect("/")
    return redirect("/")


def email(request):
    return render(request, 'email.html')

