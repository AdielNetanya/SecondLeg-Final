from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from secondleg_app import views

urlpatterns = [
                  path('', views.secondleg, name='secondleg'),
                  path('register/', views.register, name='register'),
                  path('login/', views.custom_login, name='login'),
                  path('logout/', views.custom_logout, name='custom_logout'),
                  path('list/', views.advertisement_list, name='advertisement_list'),
                  path('add/', views.add_advertisement, name='add_advertisement'),
                  path('advertisements/<int:advertisement_id>/', views.advertisement_detail,
                       name='advertisement_detail'),  # Detail view for a specific advertisement
                  path('advertisements/<int:advertisement_id>/edit/', views.advertisement_edit,
                       name='advertisement_edit'),
                  path('advertisements/<int:advertisement_id>/delete/', views.advertisement_delete,
                       name='advertisement_delete'),  # Edit view for a specific recipe
                  path('recommended-shoe/', views.recommended_shoe_list, name='recommended_shoe_list'),
                  path('recommended-shoe/add/', views.add_recommended_shoe, name='add_recommended_shoe'),
                  path('recommended-shoe/edit/<int:shoe_id>/', views.edit_recommended_shoe,
                       name='edit_recommended_shoe'),
                  path('recommended-shoe/delete/<int:shoe_id>/', views.delete_recommended_shoe,
                       name='delete_recommended_shoe'),
                  path('videos/', views.videos, name='videos'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
