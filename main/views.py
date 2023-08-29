from django.shortcuts import render,get_list_or_404,redirect,get_object_or_404

from .models import CategoryImage,PartImages
from django.contrib.auth.views import LoginView
# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

from .forms import CatForm,GalleryForm,UserForm,LoginForm

from django.contrib import messages

from urllib.parse import urlparse

from django.urls import reverse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout



def Homepage(request):

    cats = CategoryImage.objects.all()
    

    context = {'cats': cats}

    return render(request, 'main/index.html',context)



def PartImagesView(request,pk):

    category = CategoryImage.objects.filter(id=pk)
   

    parts = get_list_or_404(PartImages,category=category[0])


    

    context = {'parts': parts}

    return render(request, 'main/partimages.html',context)




def create_something(request):

    form = CatForm()
    

    if request.method == 'POST':

        print('Success')

        form = CatForm(request.POST,request.FILES)

        if form.is_valid():

          form.save()

          return redirect('home')
            

    return render(request, 'main/forms.html', {"form": form})





def delete_something(request,pk):

    cat_delete = CategoryImage.objects.filter(id=pk).first()

    cat_delete.delete()

    return redirect('home')
   









def update_something(request, pk):

    cat = get_object_or_404(CategoryImage, id=pk)

    form = CatForm(instance=cat)

    if request.method =='POST':

        form = CatForm(instance=cat, data=request.POST,files=request.FILES)

        if form.is_valid():

            form.save()

            return redirect('home')


    return render(request, 'main/update.html', {'form': form})

























def create_something_for_part(request):

    form = GalleryForm()

    if request.method == 'POST':

        form = GalleryForm(data=request.POST, files=request.FILES)

        if form.is_valid():

            form.save()

            return redirect(reverse('home'))

    return render(request, 'main/form.html', {'form':form})






def update_for_part(request,pk):

    part=PartImages.objects.get(id=pk)

    form = GalleryForm(instance=part)

    if request.method =='POST':

        form = GalleryForm(instance=part, data=request.POST, files=request.FILES)

        if form.is_valid():

            form.save()

            return redirect(reverse('home'))

    return render(request, 'main/form.html', {'form':form})






def delete_something_for_part(request,pk):

    part = PartImages.objects.filter(id=pk).first()
    part.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))













def RegistrationView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserForm()

        if request.method == 'POST':

            user = UserForm(request.POST)

            if user.is_valid():

                user.save()
                

                return redirect('home')

            
                


        return render(request, 'main/register.html', {'form': form})
        






class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = "main/login.html"
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)










def logoutView(request):
    logout(request)
    return redirect('register')