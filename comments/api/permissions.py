from rest_framework.permissions import BasePermission


## Extend the DRF Permissions Here.
class IsCommentOwnerOrReadOnly(BasePermission):
	message= "You are not allowed to be here"
	def has_object_permission(self, request, view, obj):       ## That's a static method name

		return obj.user == request.user
