from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from file_app import views
from django.conf.urls.static import static

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^upload/$',views.FileView.as_view(), name='file-upload'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)