from rest_framework import routers
from collection.views import CollectionViewSets
from profile.views import ProfileViewSets
from section.views import SectionViewSets
from post.views import PostViewSets
from comment.views import CommentViewSets

router = routers.DefaultRouter()

router.register('users', ProfileViewSets)
router.register('sections', SectionViewSets)
router.register('posts', PostViewSets)
router.register('comment', CommentViewSets)
router.register('collections', CollectionViewSets)

