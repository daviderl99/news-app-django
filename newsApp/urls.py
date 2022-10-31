from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
	path('admin/', admin.site.urls),
	path('news/', NewsView.news_list),
	path('news/<int:news_id>/', NewsView.news_detail)
]