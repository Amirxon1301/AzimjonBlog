from django.contrib import admin
from django.urls import path
from asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog),
    path('about/', about),
    path('maqola/<str:link>/', maqola),
    path('', home),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

