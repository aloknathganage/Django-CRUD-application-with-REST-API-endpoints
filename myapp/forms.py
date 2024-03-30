from django import forms

class userform(forms.Form):
    task_name = forms.CharField(max_length=20)
    task_desc = forms.CharField(max_length=50)
    iscompleted = forms.BooleanField(required=False)
    

