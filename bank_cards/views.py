from django.views.generic import CreateView

from bank_cards.cards.forms import CardForm


class CardGeneratedView(CreateView):
    form_class = CardForm
    template_name = 'generate_card.html'
