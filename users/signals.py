import os
from django.core.files import File
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

from news.models import *

@receiver(post_save, sender=User)
@transaction.atomic
def create_for_new_user(sender, instance: User, created, **kwargs):
    if created:
        image_path = os.path.join(settings.BASE_DIR, 'static', 'img', 'user.png')
        with open(image_path, 'rb') as b_img:
            image = File(b_img, f'{instance.username}.png')

            photo = Avatar.objects.create(
                user=instance,  
                image=image  
            )
            photo.save()
