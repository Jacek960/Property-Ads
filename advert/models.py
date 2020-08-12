from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name.lower().replace('ł', 'l'))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name.lower().replace('ł', 'l'))
        super(Location, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Advantages(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Surroundings(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Advert(models.Model):
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    street = models.CharField(max_length=250)
    advantages = models.ManyToManyField(Advantages, blank=True)
    surroundings = models.ManyToManyField(Surroundings, blank=True)
    area = models.PositiveIntegerField()
    no_of_rooms = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=300, blank=True, null=True)
    image1 = models.ImageField(upload_to='ad_image/', blank=True, null=True)
    image2 = models.ImageField(upload_to='ad_image/', blank=True, null=True)
    image3 = models.ImageField(upload_to='ad_image/', blank=True, null=True)
    premium = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug and self.street:
            self.slug = slugify(f"('na wynajem'-{self.category.slug}-{self.location.slug}-{self.street.lower().replace('ł', 'l')}")
        super(Advert, self).save(*args, **kwargs)



    def short_description(self):
        return self.description[:200]

    def __str__(self):
        return f'{self.location}-{self.category}-{self.street}'

