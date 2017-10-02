from django.db import models

class Publisher(models.Model):
    pubname = models.CharField(max_length=20)
    address = models.CharField(max_length=21)
    email = models.EmailField()
    # slug = models.SlugField(max_length=20,null=True)

    def __str__(self):
        return self.pubname

class Book(models.Model):
    title = models.CharField(max_length=21)
    publisher = models.ForeignKey(Publisher)
    pub_date = models.DateField()

    def __str__(self):
        return self.title
