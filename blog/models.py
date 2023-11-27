from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()


class Tag(models.Model):
    caption = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(
        validators=[MinLengthValidator(10)])
# adding a one-to-many relation using a foreign_key field
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
# adding a many-to-many relationship with the post model
    tag = models.ManyToManyField(Tag)
