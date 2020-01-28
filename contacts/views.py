from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.

def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    listing_id = request.POST['listing_id']
    consultant_email = request.POST['consultant_email']

    #Check if user has made enquiry already
    if request.user.is_authenticated: 
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing. Our team will get back to you soon, promise!')
        return redirect('/listings/'+listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name, phone=phone, message=message, user_id=user_id)

    contact.save()

    #Send mail
    send_email(
      'Property Listing Inquiry'
      'There has been an inquiry for ' + listing + '. sign into the admin panel for more info',
      'sonia.choudhury@hotmail.co.uk',
      [consultant_email, 'sonia.choudhury@hotmail.co.uk'],
      fail_silently=False
    )
  

    messages.success(request, 'Thanks, your request has been submitted and our team will get back to you soon!')
    return redirect('/listings/'+listing_id)