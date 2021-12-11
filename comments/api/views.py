## Generic Class Based API Views
from rest_framework.generics import (
		GenericAPIView,
		RetrieveAPIView                  ## Display post Detail
	)

from rest_framework.mixins import (
		ListModelMixin,
		RetrieveModelMixin,
		CreateModelMixin,
		UpdateModelMixin,
		DestroyModelMixin,
	)

from comments.models import Comment

from comments.api.serializers import (
		CommentListSerializer,
		CommentDetailSerializer,
		CommentCreateSerializer,
		CommentEditSerializer
	)


from comments.api.pagination import PostPageNumberPagination
from comments.api.permissions import IsCommentOwnerOrReadOnly      

from rest_framework.permissions import (
		IsAuthenticated,
		IsAuthenticatedOrReadOnly
	)


class CommentsListAPIView(ListModelMixin, GenericAPIView):       ## ListAPIView
	queryset= Comment.objects.all()
	serializer_class= CommentListSerializer
	pagination_class= PostPageNumberPagination


	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)



class CommentsDetailsAPIView(RetrieveModelMixin, GenericAPIView):
	queryset= Comment.objects.all()
	serializer_class= CommentDetailSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)


class CommentCreateAPIView(CreateModelMixin, GenericAPIView):
	queryset= Comment.objects.all()
	serializer_class= CommentCreateSerializer
	permission_classes= [IsAuthenticated, IsAuthenticatedOrReadOnly]

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


	def perform_create(self, serializer):
		return serializer.save(user= self.request.user)


class EditCommentMixin(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
	queryset= Comment.objects.all()
	serializer_class= CommentEditSerializer
	permission_classes= [IsAuthenticated, IsCommentOwnerOrReadOnly]

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)


	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs) 
