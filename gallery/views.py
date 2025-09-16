from django.shortcuts import render, get_object_or_404
from gallery.models import Photograph


def index(request):
    #photographs = Photograph.objects.all()
    #photographs = Photograph.objects.filter(active=True)
    
    if 'search' in request.GET:
        photographs = Photograph.objects.filter(title__icontains=request.GET['search'], active=True).order_by('-date_upload', 'title')
    else:
        photographs = Photograph.objects.order_by('-date_upload', 'title').filter(active=True)
    
    return render(request, 'gallery/index.html', {'cards': photographs})

def image(request, photo_id):
    photo = get_object_or_404(Photograph, pk=photo_id)
    return render(request, 'gallery/image.html', {'photo': photo})
