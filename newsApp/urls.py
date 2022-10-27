from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
	path('admin/', admin.site.urls),
	path('news/', NewsView.get_all),
	path('news/<int:news_id>/', NewsView.get_one)
]