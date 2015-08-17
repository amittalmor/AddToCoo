from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^locount/', include('locount.urls',namespace='locount')),         #load app:locount urls
    url(r'^$', RedirectView.as_view(url=reverse_lazy('locount:input'))),    #redirect to http://<server>/locount/input/
)
