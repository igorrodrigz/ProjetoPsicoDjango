from django import forms

class QuestionarioForm(forms.Form):
    # Cria 20 campos de escolha (sim/não)
    for i in range(1, 21):
        locals()[f'pergunta_{i}'] = forms.ChoiceField(
            choices=[('sim', 'Sim'), ('nao', 'Não')],
            widget=forms.RadioSelect,
            label=f'Pergunta {i}'
        )
    del i