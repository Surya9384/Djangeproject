from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about.html')

def category(request):
    return render(request,'category.html')

def contact(request):
    return render(request,'contact.html')

def indextwo(request):
    return render(request,'indextwo.html')

def index(request):
    return render(request,'index.html')

def post_details(request):
    return render(request,'post_details.html')

def privacy(request):
    return render(request,'privacy.html')


