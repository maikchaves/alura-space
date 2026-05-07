from django.urls import path
from gallery.views import index, image, add_image, edit_image, del_image, tag

urlpatterns = [
    path('', index, name='home'),
    path('image/<int:photo_id>', image, name='image'),
    path('add-image/', add_image, name='add_image'),
    path('edit-image/<int:photo_id>', edit_image, name='edit_image'),
    path('delete-image/<int:photo_id>', del_image, name='del_image'),
    path('tag/<str:category_name>', tag, name='tag')
]
