from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class PostLimitOffsetPagination(LimitOffsetPagination):
	default_limit= 2              ## Display 2 items per Page
	max_limit= 10


class PostPageNumberPagination(PageNumberPagination):
	page_size= 2                  ## Display 2 items per Page
	max_page_size= 10





## We Can Make This Stuff In settings.py File.
