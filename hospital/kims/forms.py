from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking 
        fields = ['name','phone','email','dep_name','doc_name','description']

        # fields = '__all__'
    
        # widgets = {
        #     'booking_date':DateInput(),
        # }

        labels = {
                'name' : "Name",
                'phone' : "Mobile Number",
                'email' : "Email",
                'dep_name' : "Department Name",
                'doc_name' : "Doctor Name",
                'description' : "Write Reasons",
            }
