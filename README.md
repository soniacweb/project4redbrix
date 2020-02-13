
![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)

<p align="center">
<img src="https://i.imgur.com/v8wV4gK.png" style="width: 500px;">
</p>

# SEI Project 4: Redbrix- A Property Search App

Redbrix is a dynamic property listings website built with Python and Django.

# Timeframe

1 week solo project

### To run

- Create a virtual environment and within the env, intall Python 3, and Django.
- python manage.py runserver inside env.

### NB terminal command for returning to your virtual env if you get kicked out after installation on mac: 
- source ./venv/bin/activate

### NB terminal command for returning to your virtual env on windows: 
- ./venv/Scripts/activate.bat (possibly absolute path)

### Technologies used:

  - Python
  - Django
  - CSS
  - HTML
  - Lightbox 2
  - Jinga 
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
- Some information about the company and property agents. Utilised with querysets and how to filter my data when I'm fetching from the database. 
- Dynamic data included in the form of Seller of the Month, 'The Team' and the 3 most recent Properties Listings.
- The listings page shows the property agent associated to that specific listing, this involves a property agent and property relationship. 
- Main image, and smaller images underneath usting the Lightbox feature.
- Underneith the main image we have some information about the proprty, ie sq ft, room number, description etc 
- There is a an enquiry button underneith the property agent's profile on this listings page. This opens up form in a modal. Its designed so if a user is already logged in, the email and name should be pre-populate from the database.
- Once registered, a message will pop using django message, and formatted in bootstrap. It also includes some javascript so that it can dissapear after 3 seconds. 

# Demo

Preview of the Lightbox feature

!['Preview of the Lightbox feature'](https://media.giphy.com/media/J4zFtwoYVQ5O6uGDyx/giphy.gif)

Enquiry on a listing, sucess message of enquiry, and dashboard summarising all enquiries once logged in:

!['Preview of the Lightbox feature'](https://media.giphy.com/media/J4zBk2EH0LW3LALuOl/giphy.gif)


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

## Pages > Views.py file for the Home and About Page: 

In this file, the methods rendered the templates. The methods take in two things- the request itself, and the location of the template. 

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

# Frontend and UI

### Page Templates  and Base Layout

##### Templates > Pages 

Two files under this folder, index.html and about.html. For the design and layout of the pages, I wanted to keep the design and theme consistant through the navigation of the site and therefore chose to extend a base layout.

***Base.html*** stored the basic design, which I could then extend to other templates. To do that, I used the Jinja syntax which is the template engine Django uses by default. 

```
</head>

  <body>

  <!-- Topbar-->
  {% include 'partials/_topbar.html' %}
  <!-- Navbar -->
  {% include 'partials/_navbar.html' %}

  <!-- Main content-->
  {% block content %} {% endblock %}

  <!-- Footer-->
  {% include 'partials/_footer.html' %}

```

Anywhere template that I required the need to extend the base layouts from, I needed to include the following: 

```
{% extends 'base.html' %}
```

Then wrap the content in a block content like so: 

```
{% block content %}
```

Before right at the end, having to include:

```
{% endblock %}
```
## Bootstrap Layout Markup and Static Files 

The entire CCS, img, webfonts, and JS folders were stored in an Asset folder.

Referencing collect static, I needed to load static assets by linking the static files to my base.html file. 

```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'btre/static')
]

```

I wanted the topbar, navbar, and footer to be present on every single page. In my base.html file, I needed to load the static files like below, referencing the folder structure and include my Bootstrap styling in: 


```
{% load static %}

...

 <link rel="stylesheet" href="{% static 'css/all.css' %}">
 <!-- Bootstrap -->
 <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
 <!-- Custom -->
 <link rel="stylesheet" href="{% static 'css/style.css' %}">
 <!-- Lightbox -->
 <link rel="stylesheet" href="{% static 'css/lightbox.min.css' %}">

 ```

# Creating a Listings and Consultants App

## urls.py: 

For both these seperate apps, I essentially repeated the same process that I did for my pages app.

I identified a path for Listings. For the single Listings page, I needed to identify a parameter:  *listings_id* is how I accessed that parameter, followed by the *views.listing* method, and the name listing.

```
urlpatterns = [
  path('', views.index, name='listings'),
  path('<int:listing_id>', views.listing, name='listing'),
  path('search', views.search, name='search'),
]
```

# PostgresSQL

I used PostGresSQL to set up my database. It's a powerful relational database, and pairs well with django, using structured query language.

I also used pgAdmin- a management tool for PostgresSQL, which gave me a graphical interface to work with. 

<img src="https://i.imgur.com/bcI0vkD.png" style="width: 600px; display:block; margin: 0 auto;">


<img src="https://i.imgur.com/9nWha9G.png" style="width: 600px; display:block; margin: 0 auto;">



# Wins

I haven't worked much with Django and Python, which is why I wanted to explore GA's last module further on my own by following a Udemy course to supplement my learning. Creating and seeding my database using Django, and feeding that through on the Boostrap frontend was a great feeling! It was an ambitious project to do on my own, but once I was slowly seeing the site come together, it was a hugely rewarding feeling. 

# Challenges 

I find deploying Django apps in general quite tricky. 


# Future Features 

Pinning properties feature included in the dashboard once logged in. 