from django.urls import path
from .views import HelloCrudView, AtletaCreationListView, AtletaDetailView, UserAtletasView, UserAtletaDetailView

urlpatterns = [
    path('', AtletaCreationListView.as_view(), name = 'atletas'),
    path('<int:atleta_id>/', AtletaDetailView.as_view(), name = 'atleta_detail'),
    path('user/<int:user_id>/atletas/', UserAtletasView.as_view(), name = 'user_atletas'),
    path('user/<int:user_id>/atleta/<int:atleta_id>/', UserAtletaDetailView.as_view(), name = 'user_atleta_detail'),
]
