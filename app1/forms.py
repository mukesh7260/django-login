from django import forms

from . models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields = '__all__'

        labels= {
           'c_id':'CUSTOMER ID',
           'name':'NAME',
           'product':'PRODUCT NAME',
           'quantity':'QUANTITY',
           'price':'PRICE'

       }