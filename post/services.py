from .models import Post
from django.conf import settings

index = settings.ES_INDEX


class PostService(object):

    @classmethod
    def save(cls, post: Post):
        return post.save()

    @classmethod
    def update(cls, post: Post):
        return post.save()

    @classmethod
    def find_posts_by_user_id(cls, id):
        return Post.filter(author=id)

    @classmethod
    def get_by_id(cls, id):
        return Post.get(id)

    @classmethod
    def delete_by_id(cls, id):
        return Post.destroy(id)
