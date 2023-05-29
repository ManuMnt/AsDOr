
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

from .forms import SignUpForm, EditForm, PasswordChangingForm
from .models import Award, Game, Wishlist, User
from django.contrib.auth.views import PasswordChangeView

def search_games(request):
    if request.method == "POST":
        searched = request.POST['searched']
        games = Game.objects.filter(name__contains = searched)
        return render(request,"games/search_games.html", {'searched': searched, 'games': games})
    else:
        return render(request,"games/search_games.html", {})

def remove_game_wishlist(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.games.remove(game)
    return redirect('games:wishlist')

def add_wishlist(request, game_id):
    game = Game.objects.get(pk=game_id)
    wishlist, created = Wishlist.objects.get_or_create(pk=request.user.id)
    wishlist.games.add(game)
    return redirect('games:wishlist')

def view_wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user).first()
    games = wishlist.games.all() if wishlist else []
    return render(request, 'accounts/wishlist.html', {'games': games})

class GamesIndexView(generic.ListView):
    template_name = 'games/index.html'
    model = Award

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        awards = Award.objects.all().select_related('game').prefetch_related('game__authors')
        years = sorted(set(award.year for award in awards), reverse=True)
        games_by_year = {}
        for year in years:
            games_by_year[year] = []
            for award in awards.filter(year=year):
                game = award.game
                authors = game.authors.all()
                category = award.category
                games_by_year[year].append({'game': game, 'authors': authors, 'category': category})
        context['games_by_year'] = games_by_year
        return context

class GameDetailView(generic.DetailView):
    model = Award
    template_name = "games/detail.html"

class UserCreationView (generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('games:login')

class UserEditionView (generic.UpdateView):
    form_class = EditForm
    template_name = "registration/edit_account.html"
    success_url = reverse_lazy('games:index')

    def get_object(self):
        return self.request.user

class PasswordChangingView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = "registration/password_change.html"
    success_url = reverse_lazy('games:password_change_done')