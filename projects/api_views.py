from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from .models import Project
from .serializers import ProjectSerializer
from accounts.mixins import AdministratorRequiredMixin
from designers.models import Designer
from designers.serializers import DesignerSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProjectListAPI(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-built_in')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'location', 'description']
    ordering_fields = ['built_in', 'name', 'contract_value']


class ProjectDetailAPI(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticated]


class ProjectCreateAPI(AdministratorRequiredMixin, generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class DesignerListAPI(generics.ListAPIView):
    queryset = Designer.objects.all()
    serializer_class = DesignerSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'profession']