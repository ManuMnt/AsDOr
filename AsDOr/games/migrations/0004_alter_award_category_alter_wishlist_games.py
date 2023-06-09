# Generated by Django 4.2 on 2023-06-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_delete_user_remove_game_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='category',
            field=models.CharField(choices=[("Jeu de l'année", 'GAME_OF_THE_YEAR'), ("Jeu de l'année 'Enfant'", 'KID_GAME_OF_THE_YEAR'), ("Jeu de l'année 'Expert'", 'EXPERT_GAME_OF_THE_YEAR'), ("Jeu de l'année 'Initié'", 'NOOB_GAME_OF_THE_YEAR'), ('Prix du Jury', 'JURY_PRIZE'), ('Grand Prix', 'BIG_PRIZE'), ('Mention Spéciale', 'MENTION_SPECIALE'), ("Super As D'Or", 'AS_OR_SUPER'), ("As D'Or", 'AS_OR'), ("As D'Or Jeu d'Imagination", 'AS_OR_IMAGINATION'), ("As D'Or Jeu Vidéo", 'AS_OR_JEU_VIDEO'), ("As D'Or Jeu de Convivialité", 'AS_OR_CONVIVIALITE'), ("As D'Or Jeu de Stratégie", 'AS_OR_STRATEGIE'), ("As D'Or Jeu d'Aventure", 'AS_OR_AVENTUREA'), ("As D'Or Jeu de Simulation", 'AS_OR_SIMULATION'), ("As D'Or Jeu d'Informatique", 'AS_OR_INFORMATIQUE'), ("As D'Or Jeu de Lettres", 'AS_OR_LETTRES'), ("As D'Or Jeu de Lettres et de Connaissances", 'AS_OR_LETTRES_CONNAISSANCES'), ("As D'Or Jeu Espoir", 'AS_OR_ESPOIR'), ("As D'Or Jeu Junior (13 - 17 ans)", 'AS_OR_JUNIOR'), ("As D'Or Jeu Benjamin (4 - 7 ans)", 'AS_OR_BENJAMIN'), ("As D'Or Jeu Cadet (8 - 12 ans)", 'AS_OR_CADET'), ("As D'Or Jeu de Société", 'AS_OR_SOCIETE'), ("As D'Or Jeu de Société d'Intéractif", 'AS_OR_SOCIETE_INTERACTIF'), ("As D'Or Jeu Joker", 'AS_OR_JOKER'), ("As D'Or Prix Spécial du Jury", 'AS_OR_SPECIAL_JURY'), ("As D'Or Jeu de Dés", 'AS_OR_DES'), ("As D'Or Jeu Innovation", 'AS_OR_INNOVATION'), ("As D'Or Jeu de Tactique", 'AS_OR_TACTIQUE'), ("As D'Or Jeu de Vocabulaire", 'AS_OR_VOCABULAIRE'), ("As D'Or Jeu de Cartes à collectionner", 'AS_OR_CARTES_COLLECTION'), ("As D'Or Jeu Familial", 'AS_OR_FAMILIALAS_OR_FAMILIAL'), ("As D'Or Jeu de la Décennie", 'AS_OR_DECENNIE'), ("As D'Or Jeu de Réfléxion", 'AS_OR_REFLEXION')], max_length=50),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='games',
            field=models.ManyToManyField(related_name='games', to='games.game'),
        ),
    ]
