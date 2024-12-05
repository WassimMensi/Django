from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.conf.urls.i18n import i18n_patterns


from blog.views import post_list, post_detail, post_create, create_category, category_list, delete_post, post_edit, signup, category_detail, toggle_favorite

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),  # Page de connexion
    path('admin/', admin.site.urls),  # Page d'administration
    path('i18n/', include('django.conf.urls.i18n')),  # Nécessaire pour 'set_language'
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),  # Page d'inscription
    path('post_list/', post_list, name='post_list'),  # Liste des articles
    path('', category_list, name='category_list'),
    path('post/<int:post_id>/toggle_favorite/', toggle_favorite, name='toggle_favorite'),
    path('categories/<slug:slug>/', category_detail, name='category_detail'),
    path('post/create_post/', post_create, name='post_create'),  # Créer un article
    path('post/create_category/', create_category, name='create_category'),  # Créer une cayégorie
    path('post/<slug:slug>/', post_detail, name='post_detail'),  # Détails d'un article
    path('post/<slug:slug>/delete/', delete_post, name='delete_post'),
    path('post/<slug:slug>/edit/', post_edit, name='post_edit'),
]


