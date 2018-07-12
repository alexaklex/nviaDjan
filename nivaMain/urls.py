from django.conf.urls import url, include
from django.contrib import admin
from nivaMain import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articls import views as art_views
# from page import views as page_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('acc.urls')),
    url(r'^articls/', include('articls.urls')),
    url(r'^page/', include('page.urls')),
    url(r'^$', art_views.articl_list, name="home"),
    url(r'^summernote/', include('django_summernote.urls')),


]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
