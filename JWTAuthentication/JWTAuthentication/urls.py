from django.contrib import admin
from django.urls import path, include
from JWT import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView

router = DefaultRouter()

#register viewset using router
# url http://localhost:8000/studentapi
router.register('studentapi',views.Studentview, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('', include(router.urls)),

]