from rest_framework import viewsets, permissions
from .models import Section
from .serializers import SectionSerializer


class SectionViewSets(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    permission_classes = (permissions.IsAuthenticated, permissions.DjangoModelPermissions)
    serializer_class = SectionSerializer
