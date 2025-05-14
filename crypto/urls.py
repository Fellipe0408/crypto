from django.contrib import admin
from django.urls import include, path
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('cotacao/', include('cotacao.urls')),
    path('sobre/', include('sobre.urls')),
    path('termo/', include('termo.urls')),
    path('formulario/', include('formulario.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('profile/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
