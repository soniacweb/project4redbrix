from django.shortcuts import render
from django.http import HttpResponse

from listings.choices import price_choices, bedroom_choices, county_choices
from listings.models import Listing
from consultants.models import Consultant


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

  return render(request, 'pages/about.html', context)