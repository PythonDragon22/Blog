## Generic Class Based API Views
from rest_framework.generics import (
		GenericAPIView,

		CreateAPIView,                   ## Just Create form
		ListCreateAPIView,               ## Create form and display posts list
		
		ListAPIView,                     ## Display posts list
		
		RetrieveAPIView,                 ## Display post Detail
		
		UpdateAPIView,                   ## Just Update Form
		RetrieveUpdateAPIView,           ## Update Form and Display The Post Data U Wanna Update
		
		DestroyAPIView,                  ## Just Delete
		RetrieveDestroyAPIView,          ## Delete and Display The Post Data U Wanna Delete
		
		RetrieveUpdateDestroyAPIView,     ## Delete and Update at the same Page
	)

from rest_framework.mixins import (
		ListModelMixin,
		RetrieveModelMixin,
		CreateModelMixin,
		UpdateModelMixin,
		DestroyModelMixin,
	)

from posts.models import (
		Posts,
		Categories,
		Tags,
	)

from posts.api.serializers import (
		PostListSerializer,
		PostSerializer,
		PostCreateSerializer,
		PostUpdateSerializer,
		CategoriesListSerializer,
		TagsListSerializer
	)

## Filter
from django.db.models import Q             ## DJango Search
from posts.api.filters import IsOwner               ## DRF Customized Search
from rest_framework.filters import (       ## DRF Search
		SearchFilter,
		OrderingFilter
	)

## Paginate
## DRF Pagination
from rest_framework.pagination import (
		LimitOffsetPagination,
		PageNumberPagination
	)
## DRF Customized Pagination
from posts.api.pagination import (
		PostLimitOffsetPagination,
		PostPageNumberPagination
	)

## Permit
## DRF Customized Permissions
from posts.api.permissions import (
		IsPostOwnerOrReadOnly,
		IsCommentOwnerOrReadOnly
	)         

## DRF Permissions
from rest_framework.permissions import (
		AllowAny,
		IsAuthenticated,
		IsAdminUser,
		IsAuthenticatedOrReadOnly
	)


class PostCreateAPIView(CreateAPIView):
	queryset= Posts.objects.all()
	serializer_class= PostCreateSerializer

	## What user is allowed to do [permissions]
	permission_classes= [IsAuthenticated]

	## Associate Post With The Author [requested user]
	## (perform_create) is a static method name
	def perform_create(self, serializer):
		return serializer.save(author= self.request.user)


class PostListAPIView(ListAPIView):
	## queryset= Posts.objects.all()
	serializer_class= PostListSerializer
	
	## Rest Filtering
	filter_backends= [SearchFilter, OrderingFilter]    ## [search and order]
	search_fields= ['title', 'content']                ## Search By Title and Content
	ordering_fields= ['id', 'created_at']              ## Order By ID and Date Created
	ordering= ['id']                                   ## The Default is Order By ID

	## Rest Pagination
	## pagination_class= LimitOffsetPagination
	pagination_class= PostPageNumberPagination

	## Filtering
	def get_queryset(self, *args, **kwargs):
		## queryset_list= super(PostListAPIView, self).get_queryset(*args, **kwargs)
		queryset_list= Posts.objects.all()
		query= self.request.GET.get('q')
		if query:
			queryset_list= queryset_list.filter(
					Q(title__icontains= query)|
					Q(content__icontains= query)
				)

		return queryset_list


class PostDetailAPIView(RetrieveAPIView):
	queryset= Posts.objects.all()
	serializer_class= PostSerializer
	lookup_field= 'slug'        ## Enable The Slug Field


class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset= Posts.objects.all()
	serializer_class= PostUpdateSerializer
	lookup_field= 'slug'
	permission_classes= [IsAuthenticated, IsPostOwnerOrReadOnly]

	## (perform_update) is a static method name
	def perform_update(self, serializer):
		return serializer.save(author= self.request.user)


class PostDeleteAPIView(RetrieveDestroyAPIView):
	queryset= Posts.objects.all()
	serializer_class= PostSerializer
	lookup_field= 'slug'
	permission_classes= [IsAuthenticated, IsPostOwnerOrReadOnly]



class UserPostsListAPIView(ListAPIView):
	queryset= Posts.objects.all()
	serializer_class= PostSerializer
	permission_classes= [IsAuthenticated, IsPostOwnerOrReadOnly]
	filter_backends= [IsOwner]
	search_fields= ['title', 'content']

	## def get_queryset(self, *args, **kwargs):
		## user= self.request.user
		## user_username= self.kwargs['username']

		## return Posts.objects.filter(author= user)
		## return Posts.objects.filter(author__username= user_username)


class CategoriesListAPIView(ListAPIView):
	queryset= Categories.objects.all()
	serializer_class= CategoriesListSerializer
	pagination_class= PostPageNumberPagination


class TagsListAPIView(ListAPIView):
	queryset= Tags.objects.all()
	serializer_class= TagsListSerializer
	pagination_class= PostPageNumberPagination
 
 
 
 
 