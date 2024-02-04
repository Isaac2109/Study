from django import forms

class MeuForm(forms.Form):

    CHOICES = (
        ('fácil', 'Fácil'),
        ('difícil', 'Difícil')
    )

    subject = forms.CharField(label='Assunto')
    difficulty = forms.ChoiceField(label='Dificuldade', choices=CHOICES)