from django.conf.urls import url, include
from django.views.generic.base import RedirectView

from . import views

company_detail_urls = [
    url(r'edit/?', views.JobRoleEdit.as_view(), name='jobRole-edit'),
    url(r'delete/?', views.JobRoleDelete.as_view(), name='jobRole-delete'),
]

company_urls = [

    url(r'new/?', views.JobRoleIndex.as_view(), name='jobRole-create'),

    url(r'^(?P<pk>\d+)/', include(company_detail_urls)),

    url(r'', views.JobRoleIndex.as_view(), name='jobRole-index'),

    # Redirect any other patterns
    url(r'^.*$', RedirectView.as_view(url='', permanent=False), name='jobRole-index'),
]