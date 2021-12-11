from rest_framework.permissions import BasePermission

class IsPostOwnerOrReadOnly(BasePermission):
	message= "You are not allowed to be here"
	def has_object_permission(self, request, view, obj):       ## That's a static method name

		return obj.author == request.user


class IsCommentOwnerOrReadOnly(BasePermission):
	message= "You are not allowed to be here"
	def has_object_permission(self, request, view, obj):       ## That's a static method name

		return obj.user == request.user

## We Can Make This Stuff In settings.py File.