from django.conf.urls import include, url
from django.contrib import admin
from sitedogs import settings
from django.conf.urls.static import static
# from django.contrib.flatpages import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('authenticate.urls')),
    # url(r'^feedback/$', views.flatpage,  {'url': '/feedback/'}, name='feedback'),
    # url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^', include('blog.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'blog.views.handler404'
