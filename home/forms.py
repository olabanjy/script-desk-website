from django import forms

class StartAProjectForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'id': 'con_name',
        'class': 'form-inp requie',
        'placeholder': 'Name'

    }))

    email = forms.CharField(required=True, widget=forms.TextInput(attrs={
    
        'id': 'con_email',
        'class': 'form-inp requie',
        'placeholder': 'Email'


    }))

    msg = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'requie',
        'id': 'con_message',
        'rows':8,
        'placeholder': 'Leave a Message!'

    }))