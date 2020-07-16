from django.shortcuts import HttpResponse , render,redirect
from django.contrib import messages
from blog.models import Contact
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from blog.models import Post
def index(request):
    post = Post.objects.all()[::-1]
    post = post[:5]
    param = {'posts':post}
    return render(request,"home/home.html",param)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        ph = request.POST.get('ph')
        msg = request.POST.get('msg')
        if len(name)<3 or len(email)<5 or len(ph)<10:
            messages.warning(request,"Please enter details correctly !")
        else:
            contact = Contact(name = name,email = email,phone = ph,message = msg)
            contact.save()
            messages.success(request,"Your message is received")


    return render(request,"home/contact.html")
def logouthandle(request):
    logout(request)
    return redirect('/')

def signup(request):        
    if request.method == "POST":
        name = request.POST.get('signupuser')
        passwd = request.POST.get('signuppass')


        #check if name exists
        try:
            all = User.objects.get(username=name)
            messages.info(request,"Username already exists. Please try another username.")
            return redirect('/')
        except:
            user = User.objects.create_user(name,None,passwd)
            user.save()
            messages.success(request,"Welcome - "+name+" - Your account has been created successfully")
            login(request,user)

            return redirect('/') 
    return HttpResponse('404 - page not found')
    
def loginhandle(request):
    if request.method == "POST":
        name = request.POST.get('loginuser')
        pas = request.POST.get('loginpass')
        user = authenticate(request,username=name,password=pas)
        if user is not None:
            login(request,user)
            messages.success(request,"Welcome back "+name+" !")
            return redirect('/')
        else:
            messages.warning(request,"Wrong username password")
            return redirect('/')
    else:
        return HttpResponse('404 - page not found')

def search(request):
    if request.method == "POST":
        search = request.POST.get('search')
        if len(search) > 70:
            print('us')
            s = Post.objects.none()
        else:
            s1 = Post.objects.filter(title__icontains=search)
            s2 = Post.objects.filter(content__icontains=search)
            s = s1.union(s2)
        if s.count() == 0:
            messages.warning(request,f"Your search - {search[:15]}... doesnot match any record")
            s = Post.objects.all()[:10]
            s = s[::-1]
        param = {'posts':s}
        return render(request,'home/search.html',param)
    else:
        return HttpResponse('404-page not found')