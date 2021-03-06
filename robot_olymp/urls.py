"""robot_olymp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    accounts/password/change/auth_password_change_done
    accounts/password/reset/confirm/OQ/set-password/auth_password_reset_complete
"""
from django.conf.urls import url, include
from django.contrib import admin
from robot_olymp import views as home_views
urlpatterns = [
    url(r'^$',home_views.home,name='home'),
    url(r'^$',home_views.index),
    url(r'^accounts/profile/$',home_views.profile, name='profile'),
    url(r'^category/sumo/$',home_views.sumo, name='sumo'),
    url(r'^category/line-follower/$',home_views.lego_line_follower, name='lego_line_follower'),
    url(r'^category/arduino-line-follower/$',home_views.arduino_line_follower, name='arduino_line_follower'),
    url(r'^category/ollo-race/$',home_views.ollo_race, name='ollo_race'),
    url(r'^category/ollo-ball/$',home_views.ollo_ball, name='ollo_ball'),
    url(r'^result/$',home_views.result, name='result'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/password/reset/auth_password_reset_done', home_views.auth_password_reset_done),
    url(r'^accounts/password/change/auth_password_change_done', home_views.auth_password_change_done),
    url(r'^accounts/password/reset/confirm/OQ/set-password/auth_password_reset_complete', home_views.password_reset_complete),
]
