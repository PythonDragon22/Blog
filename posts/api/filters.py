from rest_framework.filters import BaseFilterBackend

class IsOwner(BaseFilterBackend):
	def filter_queryset(self, request, queryset, view):       ## That's a static method name
		user= request.user

		return queryset.filter(author= user)





## fiter_queryset (filters) == get_queryset (views)