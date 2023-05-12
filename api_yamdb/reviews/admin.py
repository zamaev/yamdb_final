from django.contrib import admin

from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(GenreTitle)
admin.site.register(Review)
admin.site.register(Title)
