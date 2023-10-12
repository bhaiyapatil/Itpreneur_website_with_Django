from django.shortcuts import render,get_object_or_404
from .models import Blogs
from .models import Contact
# Create your views here.

def myblog(request):
    b = Blogs.objects.all()
    return render(request , 'blog.html' , {'b':b})

def detail(request , blog_id):
    blogdetail = get_object_or_404(Blogs , pk=blog_id)
    return render(request , 'detail.html' , {'blog':blogdetail})

def pub_date_preety(self):
    return self.pub_date.strftime('%b %e, %Y')


def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('contact')
        desc = request.POST.get('desc')
        contact = Contact(name=name , email=email , phone = phone , desc=desc)
        contact.save()
        
    return render(request , 'contact.html')
