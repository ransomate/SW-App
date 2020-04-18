from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=31)
    email = models.EmailField()
    username = models.CharField(max_length=31)
    password = models.CharField(max_length=127)
    join_date = models.DateField()
    topics_id = models.IntegerField()
    comments_id = models.IntegerField()
    picture = models.ImageField(default='')
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super(User, self).save()

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.slug)])
