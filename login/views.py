from django.shortcuts import render, redirect
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail

 
# Create your views here.
from django.shortcuts import render, redirect
from .models import Job

def home(request):
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password1']
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home1')

        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})

    else:
        return render(request, 'login.html')
    

def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        if password1 == password2: 
            try:
                user = User.objects.get(username=username)
                return render(request, 'signup.html',
                              {'error': 'Username is already taken, please choose another username'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password1, email=email)

                # Send a welcome email to the user
                subject = "Welcome to iTpreneur"
                message = f'Hi {user.username}, Thank you for registering in iTpreneur. 🚩🚩जय श्रीराम🚩🚩'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail(subject, message, email_from, recipient_list)

                return redirect('login')
        else:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'signup.html')



def home1(request):
    j = Job.objects.all()
    return render(request , 'home.html', {'j':j})


def about(request):
    return render(request , 'about.html')


################################
# views.py


def download_specific_field_pdf(request):
    data = Job.objects.values_list('pdf', flat=True)  # Query only the 'specific_field' data
    
    # Create a response with a PDF content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="specific_field_data.pdf"'

    # Create a PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Add a title to the PDF
    title = Paragraph('Specific Field Data', styles['Title'])
    story.append(title)

    # Add data to the PDF
    for field_value in data:
        paragraph = Paragraph(field_value, styles['Normal'])
        story.append(paragraph)

    # Build the PDF document
    doc.build(story)

    return response
