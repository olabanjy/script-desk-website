
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include 
from home.views import error404, error500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    

]


handler404 = error404
handler500 = error500




if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)