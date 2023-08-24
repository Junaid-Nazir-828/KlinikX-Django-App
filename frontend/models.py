from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    
    
class Testimonial(models.Model):
    image = models.ImageField(upload_to='static/testimonials')
    review = models.TextField()
    name = models.CharField(max_length=100)
    RATING_CHOICES = [
        (0, '0 Star'),
        (0.5, '0.5 Star'),
        (1, '1 Star'),
        (1.5, '1.5 Stars'),
        (2, '2 Stars'),
        (2.5, '2.5 Stars'),
        (3, '3 Stars'),
        (3.5, '3.5 Stars'),
        (4, '4 Stars'),
        (4.5, '4.5 Stars'),
        (5, '5 Stars'),
    ]
    rating = models.FloatField(choices=RATING_CHOICES)

    def __str__(self):
        return self.name

