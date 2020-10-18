from django.conf import settings
#from django.conf.urls import include
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('', include('auction.urls')),
    path('health', lambda request : HttpResponse('okay')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
