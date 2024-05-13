from django.urls import path, include
from . import views
from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView
from .views import user_login  # Correction de l'import de la vue de connexion

# Création du routeur pour les vues basées sur ViewSets
router = routers.SimpleRouter()
router.register('category', ProductViewset, basename='category')
router.register('produit', ProductViewset, basename='produit')

urlpatterns = [
    path('home/', views.index, name='index'),
    path('f/', views.form, name='majProduit'),
    path('vitrine/', views.vitrine, name='vitrine'),
    path('acc/', views.acc, name='acc'),
    path('', views.acceuil, name='acceuil'),
    path('nouvFournisseur/', views.formFournisseur, name='fournisseur'),
    path('fr/', views.fournisseur, name='fournisseur'),  # Correction du nom de la vue
    path('commande/', views.commande, name='commande'),  # Correction du nom de la vue
    path('register/', views.register, name='register'),
    path('login/', user_login, name='login'),  # Utilisation de la vue de connexion corrigée
    path('logout/', views.logoutview, name='logout'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/', include(router.urls)),
]
