from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import detail
from django.views.generic.detail import DetailView
from locount.forms import AddressForm
import models
from django.forms.util import ErrorList
from django import forms

class UserAddressView(FormView):
    template_name = 'locount/user_address.html'
    form_class = AddressForm

    def form_valid(self, form):
        obj = form.submit_address()
        if obj is not None:
            self.success_url = obj.get_absolute_url()
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList([u'Please Enter a valid address'])
            return self.form_invalid(form)
        
        return super(UserAddressView, self).form_valid(form)
        


class ShowMapView(DetailView):
    model = models.GeoAddress
    
    def get_address(self):
        return self.object.address
    
    def get_location_count(self):
        return self.object.count
    
    def get_image_source(self):
        url = 'http://maps.googleapis.com/maps/api/staticmap'
        center = '%s,%s' % (self.object.latitude,self.object.longtitude)
        markers = []
        markers.append('markers=color:red|label:.|%s,%s' % (self.object.latitude,self.object.longtitude))
        image_src = "%s?center=%s&size=1200x600&maptype=roadmap&%s&zoom=10&sensor=false" % (url,center,'&'.join(markers))
        return image_src
    
