from django import forms

class InputParam(forms.Form):
    Param1 = forms.CharField(max_length=10, label='x')
    Param2 = forms.CharField(max_length=10, label='y')

