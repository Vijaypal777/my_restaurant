from django.db import models

# Create your models here.

class ItemList(models.Model):
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name
    
class Items(models.Model):
    items_name = models.CharField(max_length=15)
    description = models.TextField(blank=False)
    price = models.IntegerField()
    category = models.ForeignKey(ItemList, related_name="items", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items/', blank=True)
    
    def __str__(self):
        return self.items_name
    
class AboutUs(models.Model):
    description = models.TextField(blank=False)
    
    def __str__(self):
        return "About Us"
    

class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    
    def __str__(self):
        return f"Feedback from {self.user_name}"
    
class BookTable(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    total_person = models.IntegerField()
    booking_date=models.DateField()
    
    def __str__(self):
        return f"Booking by {self.name}"
