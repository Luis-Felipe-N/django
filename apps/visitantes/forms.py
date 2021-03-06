from dataclasses import field
from django import forms
from visitantes.models import Visitante

class VisitanteForm( forms.ModelForm ):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "data_nascimento",
            "numero_casa", "placa_veiculo",
        ]

        error_messages = {
            "nome_completo": {
                "required": "O nome completo é obrigatório!"
            },
            "cpf": {
                "required": "O CPF é obrigatório!"
            },
            "data_nascimento": {
                "required": "A data de nascimento é obrigatória!",
                "invalid": "Por favor, insira uma data de nascimento válida! (DD/MM/AAAA)"
            },
            "numero_casa": {
                "required": "O número da casa é obrigatório!"
            }
        }

class AutorizaVisitanteForm(forms.ModelForm):

    # Aqui tambem é possivel sobrescrever os campos usando forms e não models
    morador_responsavel = forms.CharField(
        required=True
    )


    class Meta:
        model = Visitante

        fields = [
            "morador_responsavel"
        ]

        error_messages = {
            "morador_responsavel": {
                "required": "O morador resposável é obrigatório!"
            }
        }
