from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import price_choices, bedroom_choices, county_choices

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }
  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
   
  context = {
     'listing': listing
   }
  return render(request, 'listings/listing.html', context)

def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  #Keyword search
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords: 
      queryset_list = queryset_list.filter(description__icontains=keywords)

   #city 
  if 'city' in request.GET:
    city = request.GET['city']
    if city: 
      queryset_list = queryset_list.filter(city__iexact=city)

   #county isnt working
  if 'county' in request.GET:
    county = request.GET['county']
    if county: 
      queryset_list = queryset_list.filter(county__iexact=county)

   #bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms: 
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)


   #price
  if 'price' in request.GET:
    price = request.GET['price']
    if price: 
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
      'price_choices': price_choices,
      'bedroom_choices': bedroom_choices,
      'county_choices': county_choices,
      'listings': queryset_list,
      'values': request.GET
  }
  return render(request, 'listings/search.html', context)

