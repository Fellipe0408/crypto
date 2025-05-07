from django.contrib import admin
from django.urls import include, path
from django.conf import settings  # ADICIONE ESTA LINHA
from django.conf.urls.static import static  # ADICIONE ESTA LINHA

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('cotacao/', include('cotacao.urls')),
    path('sobre/', include('sobre.urls')),
    path('termo/', include('termo.urls')),
    path('formulario/', include('formulario.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # ADICIONE ESTA LINHA