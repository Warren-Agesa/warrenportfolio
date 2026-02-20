from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from django.conf import settings
from .models import Hero, SocialProfile, About, Experience, Education, Certification, PortfolioProject, PortfolioCategory, Service, ContactMessage


def index(request):
    hero = Hero.objects.first()
    social_profiles = SocialProfile.objects.all()

    context = {
        'hero': hero,
        'social_profiles': social_profiles,
    }
    return render(request, 'index.html', context)

def about_view(request):
    # Fetch the first About entry with related fields for efficiency
    about = About.objects.prefetch_related(
        'skills', 
        'hobbies', 
        'languages', 
        'social_profiles'
    ).first()
    services = Service.objects.all()
    
    return render(request, 'about.html', {
        'about': about,
        'services': services
    })



def contact(request):
      if request.method == 'POST':
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            subject = request.POST.get('subject', '').strip()
            message = request.POST.get('message', '').strip()
            
            # Validate inputs
            if not all([name, email, subject, message]):
                  return JsonResponse({'success': False, 'message': 'All fields are required'}, status=400)
            
            try:
                  # Save message to database
                  contact_msg = ContactMessage.objects.create(
                        name=name,
                        email=email,
                        subject=subject,
                        message=message
                  )
                  
                  # Get admin email from About
                  about = About.objects.first()
                  admin_email = about.email if about and about.email else 'noreply@warrenkaranja.com'
                  
                  # Send email to admin
                  email_body = f"""
New Contact Form Submission

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}

---
Sent from Warren Karanja's Portfolio
"""
                  
                  send_mail(
                        subject=f"New Portfolio Contact: {subject}",
                        message=email_body,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[admin_email],
                        fail_silently=False,
                  )
                  
                  # Send confirmation email to visitor
                  confirmation_body = f"""
Hi {name},

Thank you for reaching out! I've received your message and will get back to you as soon as possible.

Message Details:
Subject: {subject}
Sent: Now

Best regards,
Warren Karanja
"""
                  
                  send_mail(
                        subject="We've received your message",
                        message=confirmation_body,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[email],
                        fail_silently=True,
                  )
                  
                  return JsonResponse({'success': True, 'message': 'Message sent successfully! I\'ll be in touch soon.'})
            
            except Exception as e:
                  return JsonResponse({'success': False, 'message': f'Error sending message: {str(e)}'}, status=500)
      
      # Handle GET request
      about = About.objects.first()
      context = {
            'about': about
      }
      return render(request, 'contact.html', context)

def resume(request):
      experiences = Experience.objects.all()
      educations = Education.objects.all()
      certifications = Certification.objects.all()
      about = About.objects.prefetch_related('skills').first()
      
      context = {
            'experiences': experiences,
            'educations': educations,
            'certifications': certifications,
            'about': about,
      }
      return render(request, 'resume.html', context)

def services(request):
      context = {}
      return render(request, 'services.html', context)

def Portfolio(request):
      projects = PortfolioProject.objects.prefetch_related('skills', 'category').all()
      categories = PortfolioCategory.objects.all()
      featured_projects = PortfolioProject.objects.filter(is_featured=True).prefetch_related('skills')
      
      context = {
            'projects': projects,
            'categories': categories,
            'featured_projects': featured_projects,
      }
      return render(request, 'portfolio.html', context)