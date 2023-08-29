from django.urls import path
from .views import Homepage,PartImagesView,create_something,delete_something,update_something,create_something_for_part,update_for_part,delete_something_for_part,RegistrationView,CustomLoginView,logoutView
urlpatterns = [
    path('', Homepage, name='home'),
   
    path('Images/<int:pk>/',PartImagesView, name='images'),
    path('create/', create_something, name='create'),
    path('gallery/', create_something_for_part, name='gallery'),
    path('gallery/update/<int:pk>/',update_for_part, name='update-gallery'),

    path('register/',RegistrationView, name='register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
     path('log_out/', logoutView, name = 'log_out'),
    path('delete/<int:pk>/',delete_something, name='delete'),
    path('update/<int:pk>/',update_something, name='update'),
    path('picture/<int:pk>/',delete_something_for_part, name='picture'),
    


]
