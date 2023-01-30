from django.conf import settings
from django.core.mail import send_mail



class Notification:
    def __init__(self):
        pass



    def Email_notification(self,subject,message,email):
        
        self.subject=subject
        self.message=message
        self.email=email
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.email]
        send_mail(self.subject,self.message , email_from ,recipient_list )