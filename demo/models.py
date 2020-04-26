from django.db import models

# Create your models here.
class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, null=True, blank = True)
    isbn_13 = models.CharField(max_length=10, null=True, blank = True)

class Book(models.Model):
    title = models.CharField(max_length=36)
    discription = models.TextField(max_length=256, default=None)
    writter = models.CharField(max_length=36, null=True)
    name = models.CharField(max_length=36, default='NA')
    publish_date = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)
    number = models.OneToOneField(BookNumber, null = True, blank = True, on_delete = models.CASCADE)
    def __str__(self):
        return self.title
class Charecter(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete = models.CASCADE, related_name='char')

class Auther(models.Model):
    name = models.CharField(max_length=20)
    surnamename = models.CharField(max_length=20)
    book = models.ManyToManyField(Book, related_name='authname')

