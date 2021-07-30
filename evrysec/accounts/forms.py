from django import forms
 
class EmailForm(forms.Form):
    Place_Of_Incident = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required = False)
    Description = forms.CharField(widget = forms.Textarea)

