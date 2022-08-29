from django.db import models


# Create your models here.

class Publisher(models.Model):
    """Firma wydawnicza"""
    name = models.CharField(max_length=50, help_text="Nazwa wydawnictwa")
    website = models.URLField(help_text="Witryna www")
    email = models.EmailField(help_text="Adres email")

class Book(models.Model):
    """Opublikowana książka."""
    title = models.CharField(max_length=70,
                             help_text="Tytuł książki.")
    publication_date = models.DateField(
        verbose_name="Data publikacji książki.")
    isbn = models.CharField(max_length=20,
                            verbose_name="Numer ISBN książki.")

class Contributor(models.Model):
    """Współtwórca książki, np. autor, redaktor, współautor."""
    first_names = models.CharField(max_length=50,
                                   help_text="Imię lub imiona współtwórcy.")
    last_names = models.CharField(max_length=50,
                                  help_text="Nazwisko lub nawiska współtwórcy.")
    email = models.EmailField(help_text="E-mail współtwórcy.")
