from django.shortcuts import render, redirect
from .models import Category, Photo

from django.contrib.auth.decorators import login_required


from hoodapp.models import *


# Create your views here.

def gallery(request):
  category =request.GET.get('category')
  if category == None:
        photos = Photo.objects.all()
  else:
        photos = Photo.objects.filter(category__name=category)

  categories = Category.objects.all()
  context = {'categories': categories, 'photos': photos}
  return render(request, 'hoodapp/gallery.html', context)

def viewPhoto(request, cn):
  photo = Photo.objects.get(id=cn)
  return render(request, 'hoodapp/photos.html', {'photo':photo})

@login_required
def addPhoto(request):
  categories = Category.objects.all()

  if request.method == 'POST':
    data = request.POST
    image = request.FILES.get('image')

    if data['category'] != 'none':
      category = Category.objects.get(id=data['category'])
    elif data['category_new'] != '':
      category, created = Category.objects.get_or_create(
        name=data['category_new'])
    else:
      category = None

    photo = Photo.objects.create(
      category=category,
      description=data['description'],
      image=image,
    )
    return redirect('gallery')

  photo = Photo.objects.all()
  context = {'categories': categories, 'photo': photo}
  return render(request, 'hoodapp/add.html', context)

