from django import forms

class MeuForm(forms.Form):
    subject = forms.CharField(label='Assunto')
    # difficulty = forms.SelectMultiple('django/forms/widgets/select_option.html')