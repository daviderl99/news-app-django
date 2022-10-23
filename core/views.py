from rest_framework.generics import GenericAPIView
from . models import *
from rest_framework.response import Response
from . serializer import *

class NewsView(GenericAPIView):
	
	serializer_class = NewsSerializer
	queryset = ''

	def get(self, request):
		news = [
			{
				"title": news.title, 
				"date": news.date, 
				"lead": news.lead, 
				"text": news.text
			}
			for news in News.objects.all()
		]
		return Response(news)

	def post(self, request):

		serializer = NewsSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)
