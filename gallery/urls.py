from django.urls import path
from gallery.views import index, image

urlpatterns = [
    path('', index, name='home'),
    path('image/<int:photo_id>', image, name='image'),
]
