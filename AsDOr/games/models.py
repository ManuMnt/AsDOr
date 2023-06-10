from django.utils import timezone
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    wikipedia = models.URLField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Game(models.Model):
    authors = models.ManyToManyField(Author, related_name="authors")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Award(models.Model):
    CATEGORIES = [
        ("Jeu de l'année",                              "GAME_OF_THE_YEAR"),
        ("Jeu de l'année 'Enfant'",                     "KID_GAME_OF_THE_YEAR"),
        ("Jeu de l'année 'Expert'",                     "EXPERT_GAME_OF_THE_YEAR"),
        ("Jeu de l'année 'Initié'",                     "NOOB_GAME_OF_THE_YEAR"),
        ("Prix du Jury",                                "JURY_PRIZE"),
        ("Grand Prix",                                  "BIG_PRIZE"),
        ("Mention Spéciale",                            "MENTION_SPECIALE"),
        ("Super As D'Or",                               "AS_OR_SUPER"),
        ("As D'Or",                                     "AS_OR"),
        ("As D'Or Jeu d'Imagination",                   "AS_OR_IMAGINATION"),
        ("As D'Or Jeu Vidéo",                           "AS_OR_JEU_VIDEO"),
        ("As D'Or Jeu de Convivialité",                 "AS_OR_CONVIVIALITE"),
        ("As D'Or Jeu de Stratégie",                    "AS_OR_STRATEGIE"),
        ("As D'Or Jeu d'Aventure",                      "AS_OR_AVENTUREA"),
        ("As D'Or Jeu de Simulation",                   "AS_OR_SIMULATION"),
        ("As D'Or Jeu d'Informatique",                  "AS_OR_INFORMATIQUE"),
        ("As D'Or Jeu de Lettres",                      "AS_OR_LETTRES"),
        ("As D'Or Jeu de Lettres et de Connaissances",  "AS_OR_LETTRES_CONNAISSANCES"),
        ("As D'Or Jeu Espoir",                          "AS_OR_ESPOIR"),
        ("As D'Or Jeu Junior (13 - 17 ans)",            "AS_OR_JUNIOR"),
        ("As D'Or Jeu Benjamin (4 - 7 ans)",            "AS_OR_BENJAMIN"),
        ("As D'Or Jeu Cadet (8 - 12 ans)",              "AS_OR_CADET"),
        ("As D'Or Jeu de Société",                      "AS_OR_SOCIETE"),
        ("As D'Or Jeu de Société d'Intéractif",         "AS_OR_SOCIETE_INTERACTIF"),
        ("As D'Or Jeu Joker",                           "AS_OR_JOKER"),
        ("As D'Or Prix Spécial du Jury",                "AS_OR_SPECIAL_JURY"),
        ("As D'Or Jeu de Dés",                          "AS_OR_DES"),
        ("As D'Or Jeu Innovation",                      "AS_OR_INNOVATION"),
        ("As D'Or Jeu de Tactique",                     "AS_OR_TACTIQUE"),
        ("As D'Or Jeu de Vocabulaire",                  "AS_OR_VOCABULAIRE"),
        ("As D'Or Jeu de Cartes à collectionner",       "AS_OR_CARTES_COLLECTION"),
        ("As D'Or Jeu Familial",                        "AS_OR_FAMILIALAS_OR_FAMILIAL"),
        ("As D'Or Jeu de la Décennie",                  "AS_OR_DECENNIE"),
        ("As D'Or Jeu de Réfléxion",                    "AS_OR_REFLEXION")
    ]
    year = models.CharField(max_length=4)
    category = models.CharField(choices=CATEGORIES, max_length=50)
    game = models.OneToOneField(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.category + " " + str(self.year)

    class Meta:
        # Order awards by year in descending order
        ordering = ['-year']
        # Set unique constraint on category and year to enforce one award per category per year
        constraints = [
            models.UniqueConstraint(fields=['category', 'year'], name='unique_award')
        ]

    def clean(self):
        # Check that year is an integer and falls between 1988 and the current year
        current_year = timezone.now().year
        try:
            year = int(str(self.year)[:4])
            if year < 1988 or year > current_year:
                raise ValidationError({'year': 'Year must be between 1988 and the current year.'})
        except ValueError:
            raise ValidationError({'year': 'Year must be an integer.'})

    # Use custom save method to auto-populate year if not specified
    def save(self, *args, **kwargs):
        if not self.year:
            self.year = timezone.now().date()
        super().save(*args, **kwargs)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game, related_name="games")