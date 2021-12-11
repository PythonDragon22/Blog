from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

## Extend the DRF Pagination Here.
class PostPageNumberPagination(PageNumberPagination):
	page_size= 2                  ## Display 2 items per Page
	max_page_size= 10



