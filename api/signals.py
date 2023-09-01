from django.dispatch import receiver
from django.db.models import signals
from .models import Post
from django.contrib.auth.models import User

# Email object is created with all fields 
# After Configuring SMTP server it will trigger emails in live enviornment 

@receiver(signals.post_save, sender=Post)
def send_mail(sender, instance, created, **kwargs):
    if created:
        print("New Post Email Sent successfully using DJango Signals")
        # post_instance = sender.objects.filter(title=instance).values("added_by")[0]["added_by"]
        # user_instance=User.objects.filter(id=post_instance)
        # firstname=user_instance.values('first_name')[0]["first_name"]
        # subject="New post created"
        # email=user_instance.values('email')[0]["email"]
        # # send_mail(firstname, subject, email,
        # #       ['temp@mail.com'], fail_silently=False)
        



    