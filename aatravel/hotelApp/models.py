from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from Authorize.models import Partners

# Stores all the hotel details and is used to query hotels.
class Hotels(models.Model):
    #hotel_id
    Name = models.CharField(max_length  = 255)
    Address = models.CharField(max_length  = 255)
    City = models.CharField(max_length  = 255)
    Country = models.CharField(max_length  = 255)
    TelephoneNumber = models.CharField(max_length=12)
    Description = models.TextField(max_length  = 140)
    Start = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Hotels'

    def get_absolute_url(self):
        return reverse('hoteldetails', kwargs={'pk': self.pk})
    def __str__(self):
         return self.Name
# Stores the Hotel reviews and is used to query the reviews
class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    comment = models.CharField(max_length  = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default = 0)
    class Meta:
        verbose_name_plural = 'Review'

    def __str__(self):
         return self.comment
# Stores the Hotels rooms
class Room(models.Model):
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    RoomType = models.CharField(max_length  = 255)
    Capacity = models.IntegerField(default = 0)
    BedOption = models.CharField(max_length  = 255)
    Price= models.IntegerField(default = 0)
    View = models.CharField(max_length  = 255)
    TotalRooms = models.CharField(max_length  = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Room'

    def __str__(self):
         return self.RoomType

class Customer(models.Model):
    username = models.ForeignKey('auth.User', on_delete=models.CASCADE)  
    password = models.CharField(max_length = 50)
    firstName = models.CharField(max_length = 255)
    lastName = models.CharField(max_length  = 255)
    email = models.CharField(max_length = 50)
    telephone = models.CharField(max_length=12)
    class Meta:
        verbose_name_plural = 'Customer'

    def __str__(self):
         return self.username

class HotelReview(models.Model):
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    review = models.ForeignKey(Review,on_delete=models.CASCADE)
    user =  models.ForeignKey(Customer,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'HotelReview'

    def __str__(self):
         return self.review

class Order(models.Model):
    user =  models.ForeignKey(Customer,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return self.user

class Dish(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(max_length  = 255)
    price = models.IntegerField()
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    class Meta:
        verobose_name_plural = 'Dish'

    def __str__(self):
        return self.name

class DishReview(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user =  models.ForeignKey(Customer,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'DishReview'

    def __str__(self):
        return self.dish








