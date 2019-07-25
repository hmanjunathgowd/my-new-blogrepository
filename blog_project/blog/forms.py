from django import forms
class emailsendform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

from blog.models import comment
class commentform(forms.ModelForm):
    class Meta:
        model=comment
        fields=('name','email','body')
        
