from django.urls import path
from .views import UserView, LoginView, UserListByEntryDateDetailView, UserDisableView, UserUpdateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("accounts/", UserView.as_view()),
    path("login/", LoginView.as_view()),
    path("accounts/newest/<int:num>/", UserListByEntryDateDetailView.as_view()),
    path("accounts/<pk>/", UserUpdateView.as_view()),
    path("accounts/<pk>/management/", UserDisableView.as_view()),
    path("docs/", SpectacularAPIView.as_view(), name="docs"),
    path("schema/docs/", SpectacularSwaggerView.as_view(url_name="docs"), name="swagger-ui")
]