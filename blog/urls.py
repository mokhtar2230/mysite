from django.urls import path
from .views import Listeposts, DetailPost, CreerPost,ModifierPost,SupprimerPost

urlpatterns = [
    path('', Listeposts.as_view(), name='liste_post'),
    path('<int:pk>/', DetailPost.as_view(), name='detail_post'),
    path('creer/', CreerPost.as_view(), name='creer_post'),
    path('modifier/<int:pk>/', ModifierPost.as_view(), name='modifier_post'),
    path('<int:pk>/supprimer/', SupprimerPost.as_view(), name='supprimer_post'),
]
