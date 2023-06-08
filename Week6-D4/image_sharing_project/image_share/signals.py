from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Image, Profile

@receiver(post_save, sender=Image)
def update_profile_image_count(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.get(user=instance.user)
        profile.image_count = Image.objects.filter(user=instance.user).count()
        profile.save()
