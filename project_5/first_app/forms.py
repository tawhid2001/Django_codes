from django import forms

class contactForm(forms.Form):
    name = forms.CharField()
    file = forms.FileField()
    # email = forms.EmailField()
    # Age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthday = forms.DateField()
    # appointment = forms.DateTimeField()
