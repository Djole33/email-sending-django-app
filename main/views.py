from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_email = request.POST['your-email']
        your_phone = request.POST['your-phone']
        your_address = request.POST['your-address']
        starting_date = request.POST['starting-date']
        ending_date = request.POST['ending-date']
        your_message = request.POST['your-message']

        whole_message = 'Name: ' + your_name + '\n Email: ' + your_email + '\n Phone: ' + your_phone + '\n Address: ' + your_address + '\n From: ' + starting_date + '\n To: ' + ending_date + '\n Message: ' + your_message

        send_mail(
            'Message from ' + your_name, # Subject
            whole_message, # Message
            your_email, # From Email
            ['to_email.com'], # To Email
            fail_silently=False
            )
        
        return render(request, 'contact-form.html')
    
    else:
        return render(request, 'contact-form.html')
