from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
	path('admin/', admin.site.urls),
	path('news/', NewsView.as_view(), name="TestTask"),
	path('edit/', EditView.as_view(), name="EditNews")
]