from rest_framework.routers import DefaultRouter
from django.urls import path
from .company import views as company
from .accounts import views as accounts
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

app_name = 'api'

router = DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title='Snippets API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(IsAuthenticated,),
)

router.register(
    'users',
    accounts.UserViewSet,
)

router.register(
    'companys',
    company.CompanyViewSet,
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
] + router.urls
