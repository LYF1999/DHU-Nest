from rest_framework import routers
from collection.views import CollectionViewSets
from profile.views import ProfileViewSets
from section.views import SectionViewSets
from post.views import PostViewSets
from catalog.views import CatalogViewSets
# from comment.views import CommentViewSets

router = routers.DefaultRouter()

router.register('users', ProfileViewSets)
router.register('sections', SectionViewSets)
router.register('posts', PostViewSets, base_name='posts')
router.register('collections', CollectionViewSets)
router.register('catalogs', CatalogViewSets)
