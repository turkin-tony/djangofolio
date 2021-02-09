from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
import mystudio.settings as settings
from .views import home
from folio.views import view_project

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^folio/(?P<project_slug>[-\w]+)$', view_project, name='project'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
