from django.conf.urls import url

from . import views

user_urls = [
    url(r'^create-user/', views.CreateUserView.as_view(), name='create-user'),  #added by tasleem
    url(r'^update-user/(?P<pk>[a-zA-Z0-9_]+)/', views.UpdateUserView.as_view(), name='update-user'),
    url(r'^delete-user/(?P<pk>[a-zA-Z0-9_]+)/', views.DeleteUserView.as_view(), name='delete-user'),
    url(r'^activate/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.AccountActivationView.as_view(), name='acount-activate'),
    url(r'^users', views.UserListView.as_view(), name='user-list'),  # added by tasleem
]

user_api_urls = [
    url(r'token', views.GetAuthToken.as_view(), name='api-token'),
    url(r'^(?P<pk>[0-9]+)/?$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^$', views.UserList.as_view()),
    url(r'test', views.CheckPermissions.as_view(), name='api-token'),
]
# from django.conf.urls import url
# from rest_framework import routers
#
# from . import views
#
# router = routers.SimpleRouter()
# router.register(r'users', views.UserModelViewSet)
#
#
# user_urls = [
#     url(r'token', views.GetAuthToken.as_view(), name='api-token'),
#     url(r'^activate/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#         views.AccountActivationView.as_view(), name='acount-activate')
# ]
# user_urls += router.urls