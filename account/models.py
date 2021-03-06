from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

# Create your models here.


class BlogUser(User):
    last_update_date = models.DateField()
    topics_id = models.IntegerField()
    comments_id = models.IntegerField()
    captcha = CaptchaField()
    picture = models.ImageField(default='')
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super(BlogUser, self).save()

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])
