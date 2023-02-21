from django import forms

def min_lenght_3(value):
    if len(value) < 3:
        raise forms.ValidationError("Kendi denetimimiz. En az 3 karakter girmelisin..")
