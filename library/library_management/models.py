from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=32, null=False, blank=False)
    last_name = models.CharField(max_length=32, null=False, blank=False)
    birth_date = models.DateField()
    address = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Author(models.Model):
    first_name = models.CharField(max_length=32, null=False, blank=False)
    last_name = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

BOOK_GENRE = (
    ('scifi', 'Sci-Fi'),
    ('history', 'History'),
    ('classics', 'Classics'),
    ('horror', 'Horror'),
    ('kids', 'Kids'),
)


class Book(models.Model):
    name = models.CharField(max_length=512)
    year_published = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    genre = models.CharField(max_length=128, choices=BOOK_GENRE, null=True, blank=True)
    book_type = models.PositiveSmallIntegerField(default=1, null=False, blank=False)
    copies_num = models.PositiveSmallIntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    is_deleted = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
