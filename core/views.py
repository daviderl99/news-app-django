import re
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import *
from . serializer import *
class NewsView(GenericAPIView):
	serializer_class = NewsSerializer
	queryset = ''

	@api_view(['GET', 'POST'])
	def news_list(request):
		if request.method == 'GET':
			news = News.objects.all()
			serializer = NewsSerializer(news, many=True)

			return Response(serializer.data)
		elif request.method == 'POST':
			serializer = NewsSerializer(data=request.data)
			if serializer.is_valid(raise_exception=True):
				serializer.save()

			return Response(serializer.data)

	@api_view(['GET', 'PUT'])
	def news_detail(request, news_id):
		if request.method == 'GET':
			news = News.objects.get(id=news_id)
			serializer = NewsSerializer(news)

			return Response(serializer.data)
		
		elif request.method == 'PUT':
			news = News.objects.get(id=news_id)
			data = request.data

			news.title = data['title']
			news.date = data['date']
			news.lead = data['lead']
			news.text = data['text']

			news.save()
			serializer = NewsSerializer(news)
			return Response(serializer.data)