from rest_framework.serializers import (
		ModelSerializer,
		HyperlinkedIdentityField,
		SerializerMethodField,
		StringRelatedField,
	)

from posts.api.serializers import PostSerializer
from comments.models import Comment


class CommentListSerializer(ModelSerializer):
	user= StringRelatedField()
	post= StringRelatedField()

	comment_detail_url= HyperlinkedIdentityField(
			view_name= 'comments_api:comment_detail',
		)

	## comment_update_url= HyperlinkedIdentityField(view_name= 'comments_api:update_comment')

	## comment_delete_url= HyperlinkedIdentityField(view_name= 'comments_api:delete_comment')

	comment_edit_url= HyperlinkedIdentityField(view_name= 'comments_api:edit_comment')

	class Meta:
		model= Comment
		fields= (
				'id',
				'post',
				'user',
				'comment',
				'comment_detail_url',
				## 'comment_update_url',
				## 'comment_delete_url',
				'comment_edit_url',
			)


class CommentDetailSerializer(ModelSerializer):
	user= StringRelatedField()
	## post= StringRelatedField()
	post= PostSerializer(read_only= True)     ## Include The Post Detail In the Comments API Section

	class Meta:
		model= Comment
		fields= (
				'id',
				'post',
				'user',
				'comment',
			)


class CommentCreateSerializer(ModelSerializer):
	class Meta:
		model= Comment
		fields= (
				'post',
				'comment'
			)


class CommentEditSerializer(ModelSerializer):
	user= StringRelatedField()
	post= StringRelatedField()
	class Meta:
		model= Comment
		fields= ('user', 'post', 'comment',)
		read_only_fields= ('user', 'post',)




## StringRelatedField Vs. SerializerMethodField
## StringRelatedField == SerializerMethodField ++ def get_FieldName()
## SerializerMethodField can not work with a ManyToManyField
## StringRelatedField works with the ManyToManyField using (many= True) and others


