from django.contrib import admin
from .models import Author, Award, Game, Wishlist

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'wikipedia')
    ordering = ('last_name', 'first_name')


class AwardInline(admin.TabularInline):
    model = Award
    fields = ('year', 'category',)
    can_delete = False
    extra = 1


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_authors', 'get_award_category', 'get_award_year')
    search_fields = ['name', 'authors__first_name', 'authors__last_name']
    inlines = [AwardInline]

    def get_authors(self, obj):
        return ", ".join([author.__str__() for author in obj.authors.all()])
    get_authors.short_description = 'Authors'

    def get_award_category(self, obj):
        award = obj.award
        return award.category if award else ''
    get_award_category.short_description = 'Award category'
    get_award_category.admin_order_field = 'award__category'

    def get_award_year(self, obj):
        award = obj.award
        return award.year if award else ''
    get_award_year.short_description = 'Award year'
    get_award_year.admin_order_field = 'award__year'


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_games')
    search_fields = ('user__first_name', 'user__last_name')
    ordering = ('user__last_name', 'user__first_name')

    def get_games(self, obj):
        return ", ".join([game.name for game in obj.games.all()])
    get_games.short_description = 'Games'
