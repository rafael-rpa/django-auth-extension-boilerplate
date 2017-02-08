from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from apps.auth_extension import views as auth_views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', auth_views.dashboard, name='dashboard'),
    url(r'^register/$', auth_views.register, name='register'),

    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),

    url(r'^account/edit/$', auth_views.account_edit, name='account-edit'),
    url(r'^account/change-password/$', auth_views.change_password, name='change-password'),

    url(r'^password/reset/$', password_reset, {'template_name': 'password-reset-form.html', 'subject_template_name' : 'password_reset_subject.txt', 'post_reset_redirect' : '/password/reset/done/', 'html_email_template_name':'password-reset-email.html'}, name='password-reset'),
    url(r'^password/reset/done/$', password_reset_done, {'template_name': 'password-reset-done.html'}),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'password-reset-confirm.html', 'post_reset_redirect' : '/password/done/'}, name='password_reset_confirm'),
    url(r'^password/done/$', password_reset_complete, {'template_name': 'password-reset-complete.html'}),

    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
