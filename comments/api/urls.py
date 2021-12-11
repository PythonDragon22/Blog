from django.urls import path
from comments.api.views import (
		CommentsListAPIView,
		CommentsDetailsAPIView,
		CommentCreateAPIView,
		## CommentUpdateAPIView,
		## CommentDeleteAPIView
		EditCommentMixin
	)


app_name= "comments_api"
urlpatterns= [
	path('comments/', CommentsListAPIView.as_view(), name= "comment_list"),
	path('create_comment/', CommentCreateAPIView.as_view(), name= "create_comment"),
	path('comments/<int:pk>/', CommentsDetailsAPIView.as_view(), name= "comment_detail"),
	## path('comments/<int:pk>/update_comment/', CommentUpdateAPIView.as_view(), name= "update_comment"),
	## path('comments/<int:pk>/delete_comment/', CommentDeleteAPIView.as_view(), name= "delete_comment"),
	path('comments/<int:pk>/edit_comment/', EditCommentMixin.as_view(), name= "edit_comment"),
]


