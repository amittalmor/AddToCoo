from django import forms
import helpers

class AddressForm(forms.Form):
    country = forms.CharField()
    city = forms.CharField(required=False)
    street = forms.CharField(required=False)

    def submit_address(self):
        print 'submitting address:'
        lookup_address = ''
        for field in ['street','city','country']:
            val = self.data.get(field,None)
            if val is not None:
                lookup_address = '%s %s' % (lookup_address,val)
        lookup_address = lookup_address.strip()
        lat,lng = helpers.convert_address_to_lat_lon(lookup_address)
        if lat is not None and lng is not None:
            return helpers.get_or_create_geo_address(lookup_address,lat,lng)
        return None
            
            
        