from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^', include('organizer.urls')),
]
