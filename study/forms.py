from django import forms

class MeuForm(forms.Form):

    CHOICES = (
        ('fáceis', 'Fácil'),
        ('difíceis', 'Difícil')
    )

    QTD_QUESTOES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    subject = forms.CharField(label='Assunto')
    difficulty = forms.ChoiceField(label='Dificuldade', choices=CHOICES)
    number = forms.ChoiceField(label='Quantidade de questões', choices=QTD_QUESTOES)