from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
programs = Programs.objects.all()
socials = SocialIcons.objects.all()
footerabout = About.objects.all().first()

def home(request):
    context = {
        'name' : 'Samson',
        'location': 'Asaba'
    }
    products = Product.objects.all()
    
    exercise = Exercise.objects.all()
    club = OurClub.objects.all().first()
    testimonial = Testimonial.objects.all()
    

    # include products into the context dict and pass the dict to the template
    context['products'] = products
    context['programs'] = programs
    context['exercise'] = exercise
    context['our_club'] = club
    context['testimonial'] = testimonial
    context['social_icon'] = socials
    context['about_footer'] = footerabout 

    return render(request, 'index.html', context=context)

def about(request):
    context = {}
    exercise = Exercise.objects.all()
    club = OurClub.objects.all().first
    context['exercise'] = exercise
    context['programs'] = programs
    context['our_club'] = club
    context['social_icon'] = socials
    context['about_footer'] = footerabout 

    return render(request, 'about.html', context=context)

def news(request):
     context = {}
     news = News.objects.all()
     context['programs'] = programs
     context['news'] = news
     context['social_icon'] = socials
     context['about_footer'] = footerabout 

     return render(request, 'news.html',  context= context )

def contact(request):
    contact = ContactInfo.objects.all().first()

    context = {'programs': programs ,
               'social_icon': socials, 
               'about_footer': footerabout ,
               'contact_info' : contact 
               }
    
    return render(request, 'contact.html', context=context)
    

def trainer(request):
  
    return render(request, 'our-trainer.html', {'programs': programs ,'social_icon': socials, 'about_footer': footerabout   })

def program_detail(request, id):
    context = {}
    program = Programs.objects.get(id=id)
    print(id)

    context['programs'] = programs
    context['social_icon'] = socials
    context['about_footer'] = footerabout 
    context['program'] = program
    
    return render(request, 'program_details.html' , context= context)

def our_club(request):
    context = {}
    club = OurClub.objects.all().first

    context['our_club'] = club
    context['programs'] = programs
    context['social_icon'] = socials
    context['about_footer'] = footerabout 
    
    return render (request,'join_our_club.html',  context= context )
