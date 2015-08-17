from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^input/', views.UserAddressView.as_view(), name='input'),
    url(r'^maps/(?P<pk>\d+)/', views.ShowMapView.as_view(), name='map'),
)
