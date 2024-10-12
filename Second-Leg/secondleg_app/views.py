from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.uploadedfile import UploadedFile

from .forms import RecommendedShoeForm
from .forms import RegisterForm
from .forms import AdvertisementForm
from .models import Advertisement
from .models import RecommendedShoe


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


def list_advertisement(request):
    context = {
        'secondleg_text': "Welcome to SecondLeg Site"
    }
    return render(request, 'list_advertisement.html', context)


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
def advertisement_list(request):
    if request.method == "POST":
        advertisements = AdvertisementForm(request.POST)
        if advertisements.is_valid():
            advertisements.save()
            messages.success(request, "New advertisement added!")
            return redirect('advertisement_list')
    else:
        advertisements = AdvertisementForm()

    all_advertisements = Advertisement.objects.all()
    paginator = Paginator(all_advertisements, 6)  # Paginate by 5 advertisements per page
    page = request.GET.get('pg')
    all_advertisements = paginator.get_page(page)

    return render(request, 'advertisements_list.html',
                  {'all_advertisements': all_advertisements, 'advertisements': advertisements})


@login_required
def advertisement_detail(request, ad_id):
    ad = get_object_or_404(Advertisement, id=ad_id)
    return render(request, 'advertisement_detail.html', {'ad': ad})


@login_required
def advertisement_edit(request, advertisement_id):
    # Fetch the advertisement using the provided id
    advertisement = get_object_or_404(Advertisement, pk=advertisement_id)

    # Check if the user has permission to edit
    if request.user != advertisement.created_by and not request.user.is_superuser:
        return redirect('advertisement_detail', advertisement_id=advertisement.id)

    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES, instance=advertisement)

        if form.is_valid():
            # Save the form (Django will handle the image replacement automatically)
            form.save()

            return redirect('advertisement_detail', advertisement_id=advertisement.id)

    else:
        form = AdvertisementForm(instance=advertisement)

    return render(request, 'advertisement_edit.html', {'form': form, 'advertisement': advertisement})

@login_required
def advertisement_delete(request, advertisement_id):
    advertisement = get_object_or_404(Advertisement, id=advertisement_id,
                                      created_by=request.user)  # Ensure the user is the creator
    if request.method == 'POST':
        advertisement.delete()
        return redirect('advertisement_list')  # Replace with your desired redirect URL

    return render(request, 'advertisement_delete.html', {'advertisement': advertisement})


@login_required
def add_advertisement(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.created_by = request.user  # Set the user who created the ad
            ad.save()
            return redirect('advertisement_detail', ad_id=ad.id)  # Corrected line here
    else:
        form = AdvertisementForm()

    return render(request, 'add_advertisement.html', {'form': form})


def recommended_shoe_list(request):
    if request.method == 'POST':
        recommendedShoe = RecommendedShoeForm(request.POST, request.FILES)
        if recommendedShoe.is_valid():
            recommendedShoe.save()
            return redirect('recommended_shoe_list')
    else:
        recommendedShoe = RecommendedShoeForm()

    shoes = RecommendedShoe.objects.all()  # Get all recommended shoes
    return render(request, 'recommended_shoe_list.html', {'recommendedShoe': recommendedShoe, 'shoes': shoes})

@login_required
def add_recommended_shoe(request):
    if request.method == 'POST':
        recommendedShoe = RecommendedShoeForm(request.POST, request.FILES)
        if recommendedShoe.is_valid():
            shoe = recommendedShoe.save(commit=False)
            shoe.created_by = request.user
            shoe.save()
            return redirect('recommended_shoe_list')
    else:
        recommendedShoe = RecommendedShoeForm()
    return render(request, 'add_recommended_shoe.html', {'recommendedShoe': recommendedShoe})


@login_required
def edit_recommended_shoe(request, shoe_id):
    shoe = get_object_or_404(RecommendedShoe, id=shoe_id)

    if request.method == 'POST':
        form = RecommendedShoeForm(request.POST, request.FILES, instance=shoe)
        if form.is_valid():
            form.save()  # Save changes to the recommended shoe
            return redirect('recommended_shoe_list')  # Redirect to the list or detail view
    else:
        form = RecommendedShoeForm(instance=shoe)

    return render(request, 'edit_recommended_shoe.html', {'form': form})



@login_required
def delete_recommended_shoe(request, shoe_id):
    shoeToDelete = get_object_or_404(RecommendedShoe, id=shoe_id, created_by=request.user)
    if request.method == 'POST':
        shoeToDelete.delete()
        return redirect('recommended_shoe_list')
    return render(request, 'delete_recommended_shoe.html', {'shoeToDelete': shoeToDelete})


def videos(request):
    return render(request, 'videos.html')
