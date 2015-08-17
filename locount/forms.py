from django import forms
import helpers
############################################################################
# Basic (and ugly) form for entering an address
# Fields are:
# Country  ==> Mandatory
# City     ==> Optional
# Street   ==> Optional
#
# Converts an address to coordinates
# Returns a GeoAddress object or None in case the conversion has failed
############################################################################

class AddressForm(forms.Form):
    country = forms.CharField()
    city = forms.CharField(required=False)
    street = forms.CharField(required=False)

    def submit_address(self):
        # build a lookup address from the form fields
        lookup_address = ''
        for field in ['street','city','country']:
            val = self.data.get(field,None)
            if val is not None:
                lookup_address = '%s %s' % (lookup_address,val)
        lookup_address = lookup_address.strip()
        
        # convert the address to latituse and longtitude
        lat,lng = helpers.convert_address_to_lat_lon(lookup_address)
        if lat is not None and lng is not None:
            # create/update a GeoAddress objectand return it
            return helpers.get_or_create_geo_address(lookup_address,lat,lng)
        return None
            
            
        