from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from . models import *
from . serializer import *
class NewsView(GenericAPIView):
	serializer_class = NewsSerializer
	queryset = ''

	@api_view(('GET',))
	def get_all(self):
		news = News.objects.all()
		serializer = NewsSerializer(news, many=True)

		return Response(serializer.data)

	@api_view(('GET',))
	def get_one(self):
		id = 1
		news = News.objects.get(id=id)
		serializer = NewsSerializer(news)

		return Response(serializer.data)

	def post(self, request):
		serializer = NewsSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()

		return Response(serializer.data)