from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('sold', 'Sold')
    ]

    from django.db import models




# تعريف فئة Book
class Book(models.Model):
    STATUS_CHOICES = [('available', 'Available'), ('borrowed', 'Borrowed'), ('sold', 'Sold')] 

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, null=True, blank=True)
    photo_book = models.ImageField(upload_to='photos', null=True, blank=True)
    photo_author = models.ImageField(upload_to='photos', null=True, blank=True)

    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rental_price_daily = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_rental =models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rental_period = models.IntegerField(null=True, blank=True)  # إصلاح الخطأ
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title
