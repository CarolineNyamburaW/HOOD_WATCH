from django.shortcuts import render, redirect
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm
from .models import Hood, Photo

from django.contrib.auth.decorators import login_required

# Create your views here.
def register(response):
  if response.method == "POST":
    form = RegisterForm(response.POST)
    if form.is_valid():
      form.save()

    return redirect("/login")

  else:
    form = RegisterForm()

  return render(response, "register/register.html", {'form':form})

@login_required
def profile(request):
  if request.method == "POST":
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()

      return redirect("profile")

  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
 
  context = {
    'u_form': u_form,
    'p_form': p_form
  }

  return render(request, "register/profile.html", context)

@login_required
def details(request):
  return render(request, "register/details.html")


@login_required
def addHood(request):
  hoods = Hood.objects.all()

  if request.method == 'POST':
    data = request.POST
    image = request.FILES.get('image')

    if data['hood'] != 'none':
      hood = Hood.objects.get(id=data['hood'])
    elif data['hood_new'] != '':
      hood, created = Hood.objects.get_or_create(
        name=data['hood_new'])
    else:
      hood = None

    photo = Photo.objects.create(
      hood=hood,
      description=data['description'],
      image=image,
    )
    return redirect('profile')

  photo = Photo.objects.all()
  context = {'hoods': hoods, 'photo': photo}
  return render(request, 'register/addhood.html', context)