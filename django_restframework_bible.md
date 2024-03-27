-- Django Rest Framework --
	pip install djangorestframework

	-- shell -- 
		python manage.py shell
			from news.model import Article
			from news.api.serializer import ArticleSerializer
			article_instante = Article.objects.first()
			serializer = ArticleSerializer(article_instante)
			serializer.data
			from rest_framework.renderers import JSONRenderer
			json = JSONRenderer().render(serializer.data)
			import io
			from rest_framework.parsers import JSONParser
			stream = io.BytesIO(json)
			data = JSONParser().parse(stream)
			serializer = ArticleSerializer(data=data)
			serializer.is_valid()
			serializer.save()

		python manage.py shell
			from news.api.serializer import ArticleSerializer
			serializer = ArticleSerializer()
			print(repr(serializer))


-- View CBV --
	from rest_framework.views import APIView	

	class ArticleListCreateAPIView(APIView):
		def get(self, request):
			data = Article.objects.filter(active=True)
			serializer = ArticleSerializer(data, many=True)
			return Response(serializer.data)

		def post(self, request):
			serializer = ArticleSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response(status=status.HTTP_400_BAD_REQUEST)

	class ArticleDetailAPIView(APIView):
		def get_object(self, pk):
			article = get_object_or_404(Article, pk=pk)
			return article

		def get(self, request, pk):
			article = self.get_object(pk)
			serializer = ArticleSerializer(article)
			return Response(serializer.data)

		def put(self, request, pk):
			article = self.get_object(pk)
			serializer = ArticleSerializer(article, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		def delete(self, request, pk):
			article = self.get_object(pk)
			article.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)


-- View Generics e Mixins --
	from rest_framework import mixins
	from rest_framework import generics
	from rest_framework import permissions
	from ebooks.api.permissions import IsAdminUserOrReadOnly, IsAuthorOrReadOnly
	from ebooks.api.paginations import SmallSetPagination

	class EbookListCreateAPIView(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                generics.GenericAPIView):
		queryset = Ebook.objects.all()
		serializer_class = EbookSerializer

		def get(self, request, *args, **kwargs):
			return self.list(request, *args, **kwargs)

		def post(self, request, *args, **kwargs):
			return self.create(request, *args, **kwargs)


	class EbookListCreateAPIView(generics.ListCreateAPIView):
		queryset = Ebook.objects.all().order_by("id") # -id per decrescente
		serializer_class = EbookSerializer
		# permission_classes = [permissions.IsAuthenticated]
		permission_classes = [IsAdminUserOrReadOnly]
		pagination_class = SmallSetPagination

	
-- Pagination --
	from rest_framework.pagination import PageNumberPagination

	class SmallSetPagination(PageNumberPagination):
    		page_size = 3
    		page_query_param = "pagina"

	
-- Authentiction --
	pip install djoser 
	pip install requests
	pip uninstall urllib3 # per problemi ssl
	pip install 'urllib3<2.0'


-- Permission --
	from rest_framework import permissions

	class IsAuthorOrReadOnly(permissions.BasePermission):
		def has_object_permission(self, request, view, obj):
        		if request.method in permissions.SAFE_METHODS:
            			return True
        		return obj.review_author == request.user


-- Serializer --
	from rest_framework import serializers
	from ebooks.models import Ebook, Review


	class ReviewSerializer(serializers.ModelSerializer):
    		review_author = serializers.StringRelatedField(read_only=True)

    		class Meta():
        		model = Review
        		# fields = '__all__'
        		exclude = ["ebook"] 