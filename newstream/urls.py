from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

from wagtailautocomplete.urls.admin import urlpatterns as autocomplete_admin_urls

from django.urls import path
import newstream.views as user_views

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/autocomplete/', include(autocomplete_admin_urls)),
    path('admin/', include(wagtailadmin_urls)),
    path('maintenance/', user_views.maintenance, name='maintenance'),
]

urlpatterns += i18n_patterns(
    path('documents/', include(wagtaildocs_urls)),

    # path('search/', search_views.search, name='search'),

    path('donations/', include('donations.urls')),

    path('accounts/', include('allauth.urls')),

    path('personal-info/', user_views.personal_info, name='personal-info'),
    path('security/', user_views.security, name='security'),
    path('advanced-settings/', user_views.advanced_settings,
         name='advanced-settings'),
    path('advanced-settings/delete-account/', user_views.delete_account,
         name='delete-account'),
    path('unsubscribe/<email>/<hash>/', user_views.unsubscribe,
         name='unsubscribe'),
)


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    url(r'', include(wagtail_urls)),
)
