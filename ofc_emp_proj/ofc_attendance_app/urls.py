from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),              # About
    path('team.html', views.team, name='team'),                 # Team (under About dropdown)
    path('testimonials.html', views.testimonials, name='testimonials'),  # Testimonials (under About dropdown)
    path('services.html', views.services, name='services'),     # Services
    # path('services.html', views.services()),
    path('portfolio.html', views.portfolio, name='portfolio'),  # Portfolio
    path('pricing.html', views.pricing, name='pricing'),        # Pricing
    path('blog.html', views.blog, name='blog'),                 # Blog
    path('contact.html', views.contact, name='contact'),        # Contact
    # urls.py
    path('summarizer.html', views.meeting_summarizer, name='meeting_summarizer')

]
