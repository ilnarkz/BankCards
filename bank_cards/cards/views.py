from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView, UpdateView

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


class CardUpdateView(UpdateView):
    model = Card
    success_url = reverse_lazy('cards:card_detail')

    def change_status(self):
        if self.request.method == "POST":
            card = Card.objects.filter(id=self.id)
            if card.status == 'Активирована':
                card.status = 'Деактивирована'
                card.save()
            elif card.status == 'Деактивирована':
                card.status = 'Активирована'
                card.save()
        return redirect(self.success_url)
