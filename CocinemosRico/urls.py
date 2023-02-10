from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from CocinemosRico.settings import MEDIA_ROOT, MEDIA_URL

from CocinemosRico.views import index, about_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about-us/', about_us),

    path('recipes/', include('recipes.urls')),
    path('users/', include('users.urls')), 
    path('courses/', include('courses.urls')), 

]  + static(MEDIA_URL, document_root=MEDIA_ROOT)
