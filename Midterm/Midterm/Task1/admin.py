from django.contrib import admin
from .models import Restaurant, Dish, RestaurantReview, DishReview

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(RestaurantReview)
admin.site.register(DishReview)

# Register your models here.
