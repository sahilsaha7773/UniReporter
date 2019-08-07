from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('login/', views.user_login, name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('', views.home, name='home'),
	path('register/', views.register, name='register'),
	path('edit/', views.edit, name='edit'),
	path('reports/', include('reports.urls')),
	path('stories/', views.story, name='story_home'),
	path('poems/', views.poems, name='poems_home'),
	path('arts/', views.art, name='arts_home'),
	
]