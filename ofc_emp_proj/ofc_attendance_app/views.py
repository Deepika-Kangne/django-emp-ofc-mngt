from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def services(request):
    print("In services view!")
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def pricing(request):
    return render(request, 'pricing.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

from .summarizer import summarize_text  # your summarizer module

def meeting_summarizer(request):
    summary = None
    if request.method == 'POST':
        transcript = request.POST.get('transcript')
        if transcript:
            summary = summarize_text(transcript)
    return render(request, 'meeting_summarizer.html', {'summary': summary})
