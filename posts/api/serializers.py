from rest_framework.serializers import (
		ModelSerializer,
		HyperlinkedIdentityField,
		SerializerMethodField,
		StringRelatedField,
	)
from posts.models import (
		Posts,
		Categories,
		Tags,
	)


class PostListSerializer(ModelSerializer):
	detail_url= HyperlinkedIdentityField(
			view_name= 'posts_api:detail',
			lookup_field= 'slug'
		)     ## Used To Create a link To move easily Into Each Post Detail Page

	update_url= HyperlinkedIdentityField(view_name= 'posts_api:update', lookup_field= 'slug')

	delete_url= HyperlinkedIdentityField(view_name= 'posts_api:delete', lookup_field= 'slug')

	author= SerializerMethodField()   ## Turn The User ID Default Pattern Into a Username
	
	category= SerializerMethodField()

	tags = StringRelatedField(many=True)
	class Meta:
		model= Posts
		fields= [
			'id',
			'author',
			'title',
			'content',
			'detail_url',
			'update_url',
			'delete_url',
			'category',
			'tags',
			## 'slug',
			'created_at'
		]

	def get_author(self, obj):
		return str(obj.author.username)

	def get_category(self, obj):
		return str(obj.category.category_name)


class PostSerializer(ModelSerializer):
	image= SerializerMethodField()
	category= StringRelatedField()
	## tags= SerializerMethodField()
	tags = StringRelatedField(many=True)
	class Meta:
		model= Posts
		fields= [
			'id',
			'title',
			'content',
			'category',
			'tags',
			'image',
			'created_at'
		]

	def get_image(self, obj):
		try:	
			image= obj.image.url
		except ValueError:
			image= None

		return image


class PostCreateSerializer(ModelSerializer):
	category= SerializerMethodField()
	class Meta:
		model= Posts
		fields= [
			'title',
			'content',
			'category',
			'tags'
		]

	def get_category(self, obj):
		return str(obj.category.category_name)


class PostUpdateSerializer(ModelSerializer):
	category= SerializerMethodField()
	class Meta:
		model= Posts
		fields= [
			'title',
			'content',
			'category',
			'tags',
		]

	def get_category(self, obj):
		return str(obj.category.category_name)




class CategoriesListSerializer(ModelSerializer):
	class Meta:
		model= Categories
		fields= (
				'id',
				'category_name'
			)



class TagsListSerializer(ModelSerializer):
	class Meta:
		model= Tags
		fields= (
				'id',
				'tag_name'
			)



## StringRelatedField Vs. SerializerMethodField
## StringRelatedField == SerializerMethodField ++ def get_FieldName()
## SerializerMethodField can not work with a ManyToManyField
## StringRelatedField works with the ManyToManyField using (many= True) and others


