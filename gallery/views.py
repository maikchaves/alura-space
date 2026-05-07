from django.shortcuts import render, get_object_or_404, redirect
from gallery.models import Photograph
from gallery.forms import PhotographForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    #photographs = Photograph.objects.all()
    #photographs = Photograph.objects.filter(active=True)
    
    if 'search' in request.GET:
        return render(request, 'gallery/index.html', {'cards': []})
        photographs = Photograph.objects.filter(title__icontains=request.GET['search'], active=True).order_by('-date_upload', 'title')
    else:
        photographs = Photograph.objects.order_by('-date_upload', 'title').filter(active=True)
    
    return render(request, 'gallery/index.html', {'cards': photographs})


def image(request, photo_id):
    photo = get_object_or_404(Photograph, pk=photo_id)
    return render(request, 'gallery/image.html', {'photo': photo})

@login_required(login_url='login')
def add_image(request):
    if request.method == 'POST':
        photographForm = PhotographForm(request.POST, request.FILES)
        if photographForm.is_valid():
            photographForm.save()
            messages.success(request, 'Foto adicionada com sucesso!')
            return redirect('home')
    photographForm = PhotographForm()
    return render(request, 'gallery/add_image.html', {'form': photographForm})

   

def edit_image(request, photo_id):
    #photo = get_object_or_404(Photograph, pk=photo_id)
    photo = Photograph.objects.get(pk=photo_id)
    
    if request.method == 'POST':
        form = PhotographForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto editada com sucesso!')
            return redirect('home')
        
    form = PhotographForm(instance=photo)
    return render(request, 'gallery/edit_image.html', {'form': form, 'photo_id': photo_id})


def del_image(request, photo_id):
    photo = get_object_or_404(Photograph, pk=photo_id)
    if (request.user.username != 'admin' and photo.owner != request.user):
        messages.error(request, 'Você não tem permissão para excluir esta foto!')
        return redirect('home')
    Photograph.delete(Photograph.objects.get(pk=photo_id))
    messages.success(request, 'Foto excluída com sucesso!')
    return redirect('home')


def tag(request, category_name):
    photographs = Photograph.objects.order_by('-date_upload', 'title').filter(active=True, category=category_name.upper())
    return render(request, 'gallery/index.html', {'cards': photographs})