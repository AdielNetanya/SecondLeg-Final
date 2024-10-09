from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RecommendedRestaurantForm
from .forms import RegisterForm
from .forms import advertisementForm
from .models import Advertisement
from .models import RecommendedRestaurant


# Create your views here.

def index(request):
    context = {
        'index_text': "Welcome to Index page",
    }
    return render(request, 'index.html', context)


def secondleg(request):
    context = {
        'secondleg_text': "Welcome to SecondLeg Site"

    }
    return render(request, 'secondleg.html', context)


def list_recipe(request):
    context = {
        'secondleg_text': "Welcome to SecondLeg Site"
    }
    return render(request, 'list_recipe.html', context)


def contact(request):
    context = {
        'contact_text': "Welcome to Register"
    }
    return render(request, 'contact.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to a 'home' page after registration
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to a 'home' page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def custom_logout(request):
    print("custom_logout")
    print(request)
    if request.method == 'GET':
        logout(request)
        return redirect('index')  # Redirect to a 'home' page after logout
    return redirect('index')  # Fallback if accessed via GET


# views.py
def recipe_list(request):
    if request.method == "POST":
        form = advertisementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New recipe added!")
            return redirect('recipe_list')
    else:
        form = advertisementForm()

    all_recipes = Advertisement.objects.all()
    paginator = Paginator(all_recipes, 6)  # Paginate by 5 recipes per page
    page = request.GET.get('pg')
    all_recipes = paginator.get_page(page)

    return render(request, 'advertisements_list.html', {'all_recipes': all_recipes, 'form': form})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Advertisement, id=recipe_id)
    return render(request, 'advertisement_detail.html', {'recipe': recipe})


@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Advertisement, id=recipe_id)

    if request.method == "POST":
        form = advertisementForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = advertisementForm(instance=recipe)

    return render(request, 'advertisement_edit.html', {'form': form, 'recipe': recipe})


@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Advertisement, id=recipe_id, created_by=request.user)  # Ensure the user is the creator
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')  # Replace with your desired redirect URL

    return render(request, 'advertisement_delete.html', {'recipe': recipe})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = advertisementForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = advertisementForm()
    return render(request, 'add_advertisement.html', {'form': form})


def recommended_restaurant_list(request):
    if request.method == 'POST':
        form = RecommendedRestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recommended_restaurant_list')
    else:
        form = RecommendedRestaurantForm()

    restaurants = RecommendedRestaurant.objects.all()  # Get all recommended restaurants
    return render(request, 'recommended_shoe_list.html', {'form': form, 'restaurants': restaurants})


@login_required
def add_recommended_restaurant(request):
    if request.method == 'POST':
        form = RecommendedRestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.created_by = request.user
            restaurant.save()
            return redirect('recommended_restaurant_list')
    else:
        form = RecommendedRestaurantForm()
    return render(request, 'add_recommended_shoe.html', {'form': form})


@login_required
def edit_recommended_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(RecommendedRestaurant, id=restaurant_id, created_by=request.user)
    if request.method == 'POST':
        form = RecommendedRestaurantForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('recommended_restaurant_list')
    else:
        form = RecommendedRestaurantForm(instance=restaurant)
    return render(request, 'edit_recommended_shoe.html', {'form': form})


@login_required
def delete_recommended_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(RecommendedRestaurant, id=restaurant_id, created_by=request.user)
    if request.method == 'POST':
        restaurant.delete()
        messages.success(request, "Recommended restaurant deleted successfully!")
        return redirect('recommended_restaurant_list')
    return render(request, 'delete_recommended_shoe.html', {'restaurant': restaurant})


def videos(request):
    return render(request, 'videos.html')
