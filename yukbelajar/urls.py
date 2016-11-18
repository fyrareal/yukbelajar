from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from search import views as search_views
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from gallery import views as gallery_views
from wagtail.wagtailimages import urls as wagtailimages_urls
from wagtail.wagtailimages.views.serve import ServeView

urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^register/', gallery_views.register_view),
    url(r'^login/', gallery_views.login_view),
    url(r'^logout/', gallery_views.logout_view),
    url(r'^profile/', gallery_views.profile_view),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    url(r'^images/([^/]*)/(\d*)/([^/]*)/[^/]*$', ServeView.as_view(), name='wagtailimages_serve'),

    url(r'^home/', gallery_views.home_view),
    url(r'^tryout/', gallery_views.tryout_view),
    url(r'^pg/', gallery_views.pg_view),

    url(r'^api/projects/$', gallery_views.get_picture, name="gallery_rest"),
    url(r'^api/events/$', gallery_views.get_event, name="event_rest"),
    url(r'^api/project/(?P<projectid>.*.)/$', gallery_views.get_donation, name="donation_rest"),
    url(r'^confirm_donation/$', gallery_views.confirm_donation, name="confirm_donation"),

    url(r'^api/responses/$', gallery_views.get_responseCodeList, name="get_responseCodeList"),

    url(r'', include(wagtail_urls)),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
