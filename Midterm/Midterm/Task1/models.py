from django.db import models
from django.utils import timezone

class Restaurant(models.Model):
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)
    number = models.IntegerField()
    telephone = models.IntegerField()
    city = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Dish(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateField(default = timezone.now)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return "{},{},{}".format(self.rating, self.comment, self.date)
    
class RestaurantReview(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def __str__(self):
        return "{},{},{}".format(self.restaurant, self.review, self.user)

class DishReview(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete = models.CASCADE)
    review = models.ForeignKey(Review, on_delete = models.CASCADE)

    def __str__(self):
        return "{},{},{}".format(self.dish, self.review, self.user)
    


    



    


