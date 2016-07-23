from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

admin.site.site_header = u'Codesy administration'
admin.site.site_title = u'Codesy site admin'

# separating stripe, probably a django app in the future
stripe_urls = patterns(
    '',
    url(r'^update', views.StripeHookView.as_view()),
    url(r'^accept-terms', views.CreateManagedAccount.as_view()),

)

urlpatterns = patterns(
    '',
    # Static home/ explanation pages
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^offer-info$', views.OfferInfo.as_view(), name='offer-info'),
    url(r'^payout-info$', views.SaveAccountInfo.as_view(), name='payout-info'),
    url(r'^legal-info$', views.LegalInfo.as_view(), name='legal-info'),

    # allauth
    (
        r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}
    ),
    url(r'^accounts/', include('allauth.urls')),

    # admin site
    url(r'^admin/', include(admin.site.urls)),

    # auction and widget
    url(r'^', include('auctions.urls')),

    # stripe
    url(r'^stripe/', include(stripe_urls)),


    # API docs
    url(r'^api/docs/', include('rest_framework_swagger.urls')),

    # auctions API
    url(r'^', include('api.urls')),
)
