from django.urls import path
from secondleg_app import views
from django.contrib.auth import views as auth_views
from .views import recipe_list
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.secondleg, name='secondleg'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('list/',views.recipe_list, name='recipe_list'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),  # Detail view for a specific recipe
    path('recipes/<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipes/<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'), # Edit view for a specific recipe
    path('recommended-restaurants/', views.recommended_restaurant_list, name='recommended_restaurant_list'),
    path('recommended-restaurants/add/', views.add_recommended_restaurant, name='add_recommended_restaurant'),
    path('recommended-restaurants/edit/<int:restaurant_id>/', views.edit_recommended_restaurant, name='edit_recommended_restaurant'),
    path('recommended-restaurants/delete/<int:restaurant_id>/', views.delete_recommended_restaurant, name='delete_recommended_restaurant'),
    path('videos/', views.videos, name='videos'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

