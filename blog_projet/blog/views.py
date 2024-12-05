from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from django.db import models
from .forms import PostForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import logging
from django.utils.translation import gettext as _
from django.db.models import Count
from django.http import JsonResponse

logger = logging.getLogger('django')

@login_required
def toggle_favorite(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.favorites.filter(id=request.user.id).exists():
        post.favorites.remove(request.user)
        status = 'removed'
    else:
        post.favorites.add(request.user)
        status = 'added'

    return JsonResponse({'status': status})

def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    logger.info(f"Liste des articles publiés affichée")
    return render(request, 'blog/post_list.html', {'posts': posts})

# Vue pour afficher les détails d'un article
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'blog/post_detail.html', {'post': post})

# Vue pour créer un nouvel article
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Ne pas sauvegarder immédiatement
            post.author = request.user      # Attribuer l'utilisateur connecté
            post.save()                     # Sauvegarder le post avec l'auteur
            logger.info(f"Nouveau poste créer par {request.user.username}")
            return redirect('post_list')    # Redirige après la création
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})


# Vue pour créer les catégories
@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info(f"Nouvelle catégorie créée par {request.user.username}")
            return redirect('category_list')  # Redirige vers la liste des catégories (à définir)
    else:
        form = CategoryForm()
    return render(request, 'blog/create_category.html', {'form': form})

def category_list(request):
    categories = Category.objects.annotate(num_articles=Count('posts'))
    total_articles = sum(category.num_articles for category in categories)  # Calcule le total
    return render(request, 'blog/category_list.html', {
        'categories': categories,
        'total_articles': total_articles,  # Passe le total au template
    })

from django.shortcuts import get_object_or_404, redirect
from .models import Post

# Vue pour supprimer un article
@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':  # Si le formulaire de confirmation est soumis
        post.delete()
        logger.info(f"le Poste {post.title} a été supprimé par {request.user.username}")
        return redirect('post_list')  # Redirige vers la liste des articles
    return render(request, 'blog/delete_post.html', {'post': post})



@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)  # Trouver le post à éditer
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()  # Sauvegarder les modifications
            logger.info(f"le Poste {post.title} a été modifié par {request.user.username}")
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)  # Pré-remplir le formulaire avec les données du post
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement l'utilisateur après inscription
            return redirect('post_list')  # Redirige vers la liste des articles
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Post.objects.filter(category=category)

    return render(request, 'blog/category_detail.html', {
        'category': category,
        'articles': articles,
    })