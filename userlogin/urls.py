from django.conf.urls import include, url


urlpatterns = [
    url(r'^login/', 'userlogin.views.login'),
    url(r'^logout/', 'userlogin.views.logout'),
    url(r'^register/', 'userlogin.views.register'),
]
