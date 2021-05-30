from django.contrib import admin
from .models import User, TrashCan, TrashCount, Prize

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'email', 'phone_number', 'favorite_bin', 'points', 'photo_url')
    search_fields = ('name', 'surname', 'email', 'phone_number')
    list_display = ('name', 'surname', 'email', 'phone_number', 'points')


@admin.register(TrashCan)
class TrashCanAdmin(admin.ModelAdmin):
    fields = ('can_id', 'geopoint', 'status')
    search_fields = ('can_id', 'status', 'geopoint')
    list_display = ('can_id', 'geopoint', 'status')
    list_filter = ('status', )


@admin.register(TrashCount)
class TrashCountAdmin(admin.ModelAdmin):
    fields = ('user_id', 'aluminium', 'plastic', 'glass', 'paper')
    search_fields = ('user_id', )
    list_display = ('user_id', 'aluminium', 'plastic', 'glass', 'paper')

    # def get_user_id(self):
    #     result = User


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    fields = ('prize_id', 'name', 'partner_name', 'type', 'image_url')
    search_fields = ('prize_id', 'name', 'partner_name')
    list_display = ('prize_id', 'name', 'partner_name', 'type', 'image_url')
    list_filter = ('type', 'partner_name')

