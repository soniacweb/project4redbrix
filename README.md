
![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)

<img src="https://i.imgur.com/v8wV4gK.png" style="width: 500px; display:block; margin: 0 auto;">

# Project4redbrix- a Property Search Project

Redbrix is a dynamic property listings website built with Python and Django.

### To run

python manage.py runserver 


### Technologies used:

  - Python
  - Django
  - CSS
  - HTML
  - Lightbox 2
  - Posgres
  - pgAdmin

### Homepage

  - Searchbox, with features enabled. 
  - Below that the latest 3 listings in the postgres database are presented. 
- At the end we have static markups with some services listed 

<img src="https://i.imgur.com/mW1Gcme.png" style="width: 700px; display:block; margin: 0 auto;">

### Search Functionality 

<img src="https://i.imgur.com/WKZig24.png" style="width: 700px; display:block; margin: 0 auto;">

### About Page
- some information about the company and property agents. playing around with query sets and how to filter my data when im fetching from the database. 
- dynamic data included in the form of seller of the month
- the listings page shows the property agent associated to that specific listing, this involves a property agent and property relationship 
- main image, and smaller images undernieth in the form of a lightbox.
- underneith the main image we have some information about the proprty, ie sq ft, room number, description etc 
- there is a an enquiry button underneith the property agent's profile on this listins page. this opens up forn in a modal. its designed so if a user is already logged in, the email and name should pre-populate from the database.
- once registered, message will pop using django message, and formatted in bootstrap. includes some javascript so that it can dissapear after 3 seconds. 

<img src="https://i.imgur.com/B2zJ5pE.png" style="width: 700px; display:block; margin: 0 auto;">

## Dyamic Listings Page

<img src="https://i.imgur.com/SWdCvQP.png" style="width: 700px; display:block; margin: 0 auto;">

<img src="https://i.imgur.com/d1xajyt.png" style="width: 700px; display:block; margin: 0 auto;">

# Backend 

## settings.py app configuration:

Configuring the apps in settings.py is important, because it lets django recognise the below are apps. 

``` INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    'listings.apps.ListingsConfig',
    'consultants.apps.ConsultantsConfig',
    'contacts.apps.ContactsConfig',
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

```

# Paths: 

Essentially linking the *urls.py* of the respective apps I've created, to the paths.

```
urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 ```
  

### Creating the Pages App:

The pages app takes care of displaying the homepage, the about page, and any other static pages. I wanted to import modals from the 'listings' and 'consultants' app, into pages, so I can display the information from the database. This would allow for a dynamic house listings page, a 'consultant of the month' and the team- the information would be coming from the database.  

## Pages > Apps.py:
```
class PagesConfig(AppConfig):
    name = 'pages'

```

## Pages > Urls.py:

The idea here is to atttach a url path to a method inside the *views.py* file. I wanted a url path for my homepage so I defined url patterns in list format here: 

```
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
]
```

# Pages > Views.py file for the Home and About Page: 

In this file, I rendered templates here. The methods take in two things- the request itself, and the location of the template. 

```
def index(request):
   listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

   context = {
      'listings': listings,
      'price_choices': price_choices,
      'bedroom_choices': bedroom_choices,
      'county_choices': county_choices
   }

   return render(request, 'pages/index.html', context)

def about(request): 
  #get all consultants
  consultants = Consultant.objects.order_by('-hire_date')
```

Seller of the month has mvp check- this will allow the client to select who they would like to be highlighted on the backend, which will get rendered in the *Abouts* page on the frontend. There can be more than one consultant selected. 

```
  mvp_consultants = Consultant.objects.all().filter(is_mvp=True)

  context = {
      'consultants': consultants,
      'mvp_consultants': mvp_consultants
   }
  
  ``` 

# Frontend

### Page Templates  and Base Layout

##### Templates > Pages 

Two files under this folder, index.html and about.html. 



# Challenges 


# Future Features 

Pinning properties feature included in the dashboard once logged in. 