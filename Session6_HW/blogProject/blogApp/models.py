from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=10)
    address = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    edittime = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
