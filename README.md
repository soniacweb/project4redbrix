
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

### For returning to your virtual env on windows: 
- ./venv/Scripts/activate.bat (possibly absolute path)

### Technologies used:

  - Python
  - Django
  - CSS
  - HTML
  - Lightbox 2
  - Jinga 
  - Postgres
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


Enquiry on a listing, success message of enquiry, and dashboard summarising all enquiries once logged in:

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

<img src="https://i.imgur.com/bcI0vkD.png" style="width: 500px; display:block; margin: 0 auto;">


<img src="https://i.imgur.com/9nWha9G.png" style="width: 500px; display:block; margin: 0 auto;">

I had to implement Postgres into my Django app by defining the parameters in the settings file, but I also needed to install a couple of packages using pip in my venv.

- pip install psyocopg2
- pip install psyocopg2-binary

And in my root btre, settings.py I set up the parameters and included the following: 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'redbrixdb',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '6000'
    }
}
```

To get Postgres to interact with my django app, I migrated my apps using `python manage.py migrate`, where they were visible in pgAdmin (see above screenshot).

This is how I connected to my database, and I could now think about my models, schemas, my own migrations to create tables and listings. 

# Planning and mapping out my schemas

Before creating my modals, I drafted out my schemas with what I would need for my site, and what the relationships would be.

## Listings DB Table 

| MODALS | DB FIELDS |
| ------ | ------ |
| id | INT |
| Consultant | INT (it will be a foreign key field from the consultant's table (and all of the respective fields like their name, contact details, photo etc) and associate that to a listing. |
| Title | Str- probably first line of street |
| City | Str|
| County| Str |
| Description | Text (text field- as the description of properties will be longer) |
| Price| Int |
| Price| Int |
| Bedrooms| Int |
| Garage | Int |
| Sqft | Int |
| Lot_size | Float (decimal) |
| List_date| Date |
| Photo_main | Str |
| Photo_1 | Str |
| Photo_2 | Str |
| Photo_3 | Str |
| Photo_4 | Str |
| Photo_5| Str |
| Photo_6| Str |

As an fyi, I didn't store images in the database, but stored the location of the images. That way I could fetch the location of the image and simply put that into an image source and render it on the page.  


## Consultant Database

| MODALS | DB FIELDS |
| ------ | ------ |
| id | INT |
| Name | Str |
| Photo | Str|
| Description | Text|
| Email| Str |
| is_mvp | BOOL |


## Contact (any enquiry that's made to the application on any of the listings should be saved in the database in a contact table)

| MODALS | DB FIELDS |
| ------ | ------ |
| id | INT |
| User_id| INT |
| Name of the listing | INT |
| Name  | Str |
| Email |  Str |
| Phone | Str |
| Message | Text |
| Contact Date | Date | 

# Creating my Models

After creating these, I ran a migration to create the tables in my database based on the models.  

This is the model for my listings app. Found in *Listings > models.py* : 

```
class Listing(models.Model):
  consultant = models.ForeignKey(Consultant, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  county = models.CharField(max_length=100)
  postcode = models.CharField(max_length=10)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title
  ```

# Creating a Superuser And Registering Models with Admin

`python manage.py createsuperuser` in my virtual environment through the integrated terminal allowed me to create a superuser. 

<img src="https://i.imgur.com/uIbu5pf.png" style="width: 550px; display:block; margin: 0 auto;">

# Fetching Data and displaying it on the Frontend

I wanted to loop through my listings and output on the frontend. I  used a for loop using the jinja template syntax in my templates folder, inside listings.html. I wanted each one of my listings to have the same markup, but the information fetched from the database to be dynamic through the use of dynamic variables passing through every iteration of the loop. I accessed my properties in my database, through the use of dot notation in this syntax: `{{ listing.title }}` for example. 

This rendered unique listed properties on the frontend for my listings page. 

```

<section id="listings" class="py-4">
  <div class="container">
    <div class="row">
      {% if listings %}
      {% for listing in listings %}

 <!-- Listing 1 -->
 <div class="col-md-6 col-lg-4 mb-4">
  <div class="card listing-preview">
    <img class="card-img-top" src="{{ listing.photo_main.url }}" alt="">
    <div class="card-img-overlay">
      <h2>
        <span class="badge badge-danger text-white">£{{ listing.price | intcomma }}</span>
      </h2>
    </div>
    <div class="card-body"> 
      <div class="listing-heading text-center">
        <h4 class="text-primary">{{ listing.title }}</h4>
        <p>
          <i class="fas fa-map-marker text-dark"></i> {{ listing.city }} {{ listing.county }} {{ listing.postcode }} </p>
      </div>
      <hr>
      <div class="row py-2 text-dark">
        <div class="col-6">
          <i class="fas fa-th-large"></i> Square ft: {{ listing.sqft }} </div>
        <div class="col-6">
          <i class="fas fa-car"></i> {{ listing.garage}} </div>
      </div>
      <div class="row py-2 text-dark">
        <div class="col-6">
          <i class="fas fa-bed"></i> Bedrooms: {{ listing.bedrooms }} </div>
        <div class="col-6">
          <i class="fas fa-bath"></i> Bathrooms: {{ listing.bathrooms }} </div>
      </div>
      <hr>
      <div class="row py-2 text-dark">
        <div class="col-12">
          <i class="fas fa-user"></i> {{ listing.consultant }} </div>
      </div>
      <div class="row text-dark pb-2">
        <div class="col-6">
          <i class="fas fa-clock"></i> {{ listing.list_date | timesince }} </div>
      </div>
      <hr>
      <a href="{% url 'listing' listing.id %}" class="btn btn-danger btn-block">More Info</a>
    </div>
  </div>
</div>
  {% endfor %}
    {% else %}
 <div class="col-md-12">
  <p>No Listings Available</p>
 </div>
      {% endif %}  

</div>
    <div class="row">
      <div class="col-md-12">
        {% if listings.has_other_pages %}
          <ul class="pagination">
           {% if listings.has_previous %}
              <li class="page-item">
              <a href="?page={{listings.previous_page_number}}" class="page-link">&laquo;
              </a>
            </li>
            {% else %}
              <li class="page-item disabled">
                <a class="page-link">&laquo;</a>
              </li>
          {% endif %}
          {% for i in listings.paginator.page_range %}
          {% if listings.number == i %}
          <li class="page-item activate">
            <a href="" class="page-link">{{i}}</a>
          </li>
          {% else %}
          <li class="page-item">
            <a href="?page={{i}}" class="page-link">{{i}}</a>
          </li>
            {% endif %}
          {% endfor %}

  ```

I used the same method to create dynamic information in the Home and Abouts page. 

# Single Listings Page 

Using virtually the same method as above, I needed to work with two documents here, the method I had already identified and the markup for the template.

Listings > views.py
Template > listing.html

# Search Feature 

# Register and Login

# Contact Inquiries and Dashboard Feature 


# Wins

I haven't worked much with Django and Python, which is why I wanted to explore GA's last module further on my own by following a Udemy course to supplement my learning. Creating and seeding my database using Django, and feeding that through on the Boostrap frontend was a great feeling! It was an ambitious project to do on my own, but the highlight for me, was strangely the Inquiries and Dashboard features. All in all, once I was slowly seeing the site come together, it was a hugely rewarding feeling. 

# Challenges 

I find deploying Django apps in general quite tricky. 


# Future Features 

- Refactor frontend using React
- I would like to incorporate a 'pinning' feature for users to pin properties of interest, and display them on the dashboard once logged in. 