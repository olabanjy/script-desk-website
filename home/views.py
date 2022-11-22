from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives, send_mail, EmailMessage
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils.encoding import force_bytes
from django.views.defaults import page_not_found
from .forms import *


# Create your views here.

def error404(request, exception):
    return page_not_found(request, exception, 'errors/404.html')

def error500(request):
    return render(request, 'errors/500.html')

def homepage(request):
        
    template = 'home/index.html'
    
    return render(request, template)

def aboutus(request):
        
    template = 'home/about.html'
    
    return render(request, template)

class StartAProject(View):
    
    def get(self, request, *args, **kwargs):
        template = 'home/contact.html'

        form = StartAProjectForm()

        context = {
            'form': form
        }

        return render(self.request, template, context)

    def post(self, request, *args, **kwargs):

        form = StartAProjectForm(self.request.POST or None)

        try:
            if form.is_valid():
                name = form.cleaned_data.get('name')
                email = form.cleaned_data.get('email')
                msg = form.cleaned_data.get('msg')

                subject, from_email, to = 'New Project Entry from Website', 'SCRIPT DESK <dev@scriptdeskng.com>', ['shola.albert@gmail.com', 'hello@scriptdeskng.com', 'biz@scriptdeskng.com']
                
                html_content = render_to_string(
                    'home/email_from_site.html', {'email': email, 'name': name, 'msg': msg })
                msg = EmailMessage(subject, html_content, from_email, to)
                msg.content_subtype = "html"
                msg.send()

                return redirect('home:thank-you')

        except (ValueError, NameError, TypeError) as error:
            err_msg = str(error)
            print(err_msg)
        except:
            print("Unexpected Error")
            raise

def thankyou(request):

    template = 'home/thankyou.html'

    return render(request, template)