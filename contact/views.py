import ssl

from django.shortcuts import render

from django.conf import settings
from .models import Info
from django.core.mail import get_connection, send_mail
# Create your views here.


def send_massage(request):
    myInfo = Info.objects.first()
    
    if request.method == 'POST':
        
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')

        # context = ssl._create_unverified_context()
        # context.check_hostname = False 
        # context.verify_mode = ssl.CERT_NONE
        
        
        # connection = get_connection(
        #     backend='django.core.mail.backends.smtp.EmailBackend',
        #     # context=context
        # )
        # try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            # connection=connection
        )
        
        # except Exception as e:
        #     print(f"Error: {e}")
    return render(request, 'contact/contact.html', {'myInfo': myInfo})
