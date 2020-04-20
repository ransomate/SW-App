from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(default='', blank=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse('tag', args=[str(self.pk)])


class Post(models.Model):
    title = models.CharField(max_length=255, default='', unique=True)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(default='', blank=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    body = models.TextField(default='', blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(default='', blank=True, upload_to='post_images')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(250, 100)],
                                     format='JPEG',
                                     options={'quality': 60})

    image_large = ImageSpecField(source='image',
                                 processors=[ResizeToFill(700, 250)],
                                 format='JPEG',
                                 options={'quality': 60})

    class Meta:
        ordering = ['-post_date']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse('item', args=[str(self.pk)])


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
