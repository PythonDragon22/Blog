from django.urls import path
from posts.api.views import (
		PostListAPIView,
		PostDetailAPIView,
		PostUpdateAPIView,
		PostDeleteAPIView,
		PostCreateAPIView,
		UserPostsListAPIView,
		CategoriesListAPIView,
		TagsListAPIView,
	)


app_name= "posts_api"
urlpatterns= [
	path('create/', PostCreateAPIView.as_view(), name= "create"),
	path('tags/', TagsListAPIView.as_view(), name= "tags"),
	path('categories/', CategoriesListAPIView.as_view(), name= "categories"),
	path('user_posts/', UserPostsListAPIView.as_view(), name= "user_posts"),

	path('', PostListAPIView.as_view(), name= "list"),


	## path('<int:pk>/', ArticlesDetailAPIView.as_view(), name= "detail"),
	path('<str:slug>/', PostDetailAPIView.as_view(), name= "detail"),
	path('<str:slug>/update/', PostUpdateAPIView.as_view(), name= "update"),
	path('<str:slug>/delete/', PostDeleteAPIView.as_view(), name= "delete"),


	## path('<str:slug>/update_delete/', PostUpdateDeleteAPIView.as_view(), name= "update_delete"),
]



