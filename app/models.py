from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Author'
    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Book'
    def __str__(self):
        return self.name

