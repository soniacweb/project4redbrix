from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.

def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # to check if passwords match: .exists() is a helpful method that'll let me know if the username already exists
    if password == password2:
      # check username
      if User.objects.filter(username=username).exists():
       messages.error(request, 'That username already exists, please login.')  
       return redirect('register')
      else: #check email already exists
        if User.objects.filter(email=email).exists():
         messages.error(request, 'This email already exists, please login.')  
         return redirect('register')
        else: 
          #looks goods
          user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          #login after register
          user.save()
          messages.success(request, 'You\'re now registered')
          return redirect('login')
    else: 
      messages.error(request, 'Passwords don\'t match')
      return redirect('register')
  else:  
    return render(request, 'accounts/register.html')
  
def login(request):
  if request.method == 'POST':
   #login  user logic 
   username = request.POST['username']
   password = request.POST['password']
   
   user = auth.authenticate(username=username, password=password)
   if user is not None: #this means if the user is found in the database
    auth.login(request, user)
    messages.success(request, 'You\'re now logged in')
    return redirect('dashboard') 
   else: 
    messages.error(request, 'Invalid credentials')
    return redirect('login')
  else:    
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'Thanks for stopping by. You\'re now logged out.' )
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')