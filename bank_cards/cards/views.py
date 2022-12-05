from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView

from bank_cards.cards.models import Card


class CardListView(ListView):
    model = Card
    template_name = 'card_list.html'

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        if query:
            object_list = Card.objects.filter(Q(card_series__icontains=query) | Q(card_number__icontains=query))
        else:
            object_list = Card.objects.all()
        return object_list


class CardDetailView(DetailView):
    model = Card
    template_name = 'card_detail.html'


class CardDeleteView(DeleteView):
    model = Card
    template_name = 'card_delete.html'
    success_url = reverse_lazy('cards:card_list')


def update_status(request, pk):
    card = Card.objects.get(pk=pk)
    if card.status == 'Активирована':
        Card.objects.filter(pk=pk).update(status='Деактивирована')
    elif card.status == 'Деактивирована':
        Card.objects.filter(pk=pk).update(status='Активирована')
    return redirect('cards:card_list')
