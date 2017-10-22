from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from nummadekochi.core import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.main, name="main"),
    url(r'^donate$', core_views.donate, name="donate"),
    url(r'^about-us$',core_views.about, name="about_us"),
    url(r'^stories$', core_views.stories, name="story"),
    url(r'^contact_us$', core_views.contact_us, name="contact_us"),
    url(r'^donate/(?P<id>[0-9].*)$',core_views.donateview,name="donate_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                                        document_root=settings.MEDIA_ROOT)
