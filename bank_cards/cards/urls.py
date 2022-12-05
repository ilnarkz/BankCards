from django.urls import path

from bank_cards.cards import views

app_name = 'cards'

urlpatterns = [
    path('', views.CardListView.as_view(), name='card_list'),
    path('<int:pk>/', views.CardDetailView.as_view(), name='card_detail'),
    path('<int:pk>/delete/', views.CardDeleteView.as_view(), name='card_delete'),
    path('<int:pk>/update/', views.CardUpdateView.as_view(), name='update_status'),
]
