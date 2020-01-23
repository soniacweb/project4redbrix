from django.contrib import admin

from .models import Listing 

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'consultant')
  list_display_links = ('id', 'title', 'price', 'list_date', 'consultant')
  list_filter = ('consultant', 'is_published')
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'postcode', 'county', 'city', 'price', 'list_date')
  list_per_page = 25
  
admin.site.register(Listing, ListingAdmin)
 