
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
  

### Creating the Pages Apps:

The pages app takes care of displaying the homepage, the about page, and any other static pages. I wanted to import modals from the 'listings' and 'consultants' app, into pages, so I can display the information from the database. This would allow for a dynamic house listings page, a 'consultant of the month' and the team- the information would be coming from the database.  

## apps.py:
```
class PagesConfig(AppConfig):
    name = 'pages'

```

## urls.py:

The idea here is to atttach a url path to a method inside the *views.py* file. I wanted a url path for my homepage so I defined url patterns in list format here: 

```
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
]
```

## views.py file: 

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

  #seller of the month has mvp check
  mvp_consultants = Consultant.objects.all().filter(is_mvp=True)

  context = {
      'consultants': consultants,
      'mvp_consultants': mvp_consultants
   }
  
  ``` 



### Tech

Dillinger uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [markdown-it] - Markdown parser done right. Fast and easy to extend.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [Breakdance](https://breakdance.github.io/breakdance/) - HTML to Markdown converter
* [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Installation

Activating the viertual environment: source ./venv/bin/activate

Dillinger requires [Node.js](https://nodejs.org/) v4+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ NODE_ENV=production node app
```

### Plugins

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |


### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version} .
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

#### Kubernetes + Google Cloud

See [KUBERNETES.md](https://github.com/joemccann/dillinger/blob/master/KUBERNETES.md)


### Todos

 - Write MORE Tests
 - Add Night Mode

License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

  
