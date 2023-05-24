from django.urls import include, path
from . import views

app_name = "games"

urlpatterns = [
  path("", views.GamesIndexView.as_view(), name="index"),
  path("<int:pk>/", views.GameDetailView.as_view(), name="detail"),
  path("<user_id>/password/", views.PasswordChangingView.as_view(), name="password_change"),
  path("search/", views.search_games, name="search"),
  path('accounts/', include('django.contrib.auth.urls')),
  path("accounts/edit/", views.UserEditionView.as_view(), name="edit"),
  path("accounts/signup/", views.UserCreationView.as_view(), name="signup"),
  path("accounts/wishlist/", views.view_wishlist, name="wishlist"),
  path("accounts/wishlist/add_wishlist/<game_id>/", views.add_wishlist, name="add-wishlist"),
  path("accounts/wishlist/remove_game_wishlist/<game_id>/", views.remove_game_wishlist, name="remove-game-wishlist"),
]