from django.forms import ModelForm

from bank_cards.cards.models import Card


class CardForm(ModelForm):

    class Meta:
        model = Card
        fields = ['how_long', 'status']
