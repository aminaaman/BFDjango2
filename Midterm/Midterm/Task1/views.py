from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Restaurant, Dish, Review, RestaurantReview, DishReview
from django.http import HttpResponse

def review(request):
    review_list=Restaurant.objects.order_by('id')
    context = {'review_list': review_list}
    return render(request, 'reviews.html', context)
# Create your views here.
