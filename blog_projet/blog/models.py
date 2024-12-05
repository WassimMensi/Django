from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    # Champs du modèle
    name = models. CharField(max_length=100, verbose_name=_("Nom")) # Champ texte Limité à 100 caractères
    slug = models.SlugField(unique=True) # URL-friendly version du nom (unique)
    description = models. TextField(blank=True) # Texte Long optionnel
    created_at = models.DateTimeField(auto_now_add=True) # Date de création automatique

    class Meta:

        verbose_name_plural = 'categories' # Nom au pluriel dans l'admin
        ordering = ['name' ] # Tri par nom

    def __str__(self):
        return self.name # Représentation texte de la catégorie

    def get_absolute_url(self):
        # Génère L'URL de la catégorie
        return reverse('category-detail', kwargs={'slug': self.slug})

class Tag(models.Model):
    # Champs du modèle
    name = models. CharField(max_length=100) # Champ texte Limité à 100 caractères
    slug = models.SlugField(unique=True) # URL-friendly version du nom (unique)
    created_at = models.DateTimeField(auto_now_add=True) # Date de création automatique

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Titre"))
    content = models.TextField(verbose_name=_("Contenu"))
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=200, verbose_name=_("Titre"))
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name=_("Contenu"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    image = models.ImageField(upload_to='blog_images/%Y/%m/%d/', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def is_favorited_by(self, user):
        return user in self.favorites.all()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
