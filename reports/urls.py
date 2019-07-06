from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = "reports"
urlpatterns = [
	path('create/', views.report_create, name='create'),
	path('detail/<int:id>/<slug:slug>/', views.report_detail, name='detail'),
]