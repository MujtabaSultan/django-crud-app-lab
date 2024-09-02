from django.urls import path,include
from . import views # Import views to connect routes to view functions

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  # route for cats index
  path('cars/', views.car_index, name='car-index'),
  path('cars/<int:car_id>/', views.car_detail, name='car-detail'),
  path('cars/create/', views.CarCreate.as_view(), name='car-create'),
  path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car-update'),
  path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'),
  path('modification/create/', views.ModificationCreate.as_view(), name='modification-create'),
  path('modifications/<int:pk>/', views.ModificationDetail.as_view(), name='modification-detail'),
  path('modifications/', views.ModificationList.as_view(), name='modification-index'),
  path('modifications/<int:pk>/update', views.ModificationUpdate.as_view(), name="modification-update"),
  path('modifications/<int:pk>/delete', views.ModificationDelete.as_view(), name="modification-delete"),
  path('cars/<int:car_id>/associate-modification/<int:modification_id>', views.associate_modification, name='associate-modification'),
  path('cars/<int:car_id>/remove-modification/<int:modification_id>/', views.remove_modification, name='remove-modification'),
  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/', include('django.contrib.auth.urls')),
  
  
  
 ]
   
