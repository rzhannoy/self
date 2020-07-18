from django.contrib import admin

from .models import Message, Post, Subscriber


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_processed', 'created']
    list_filter = ['is_processed']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_hidden', 'created']
    list_filter = ['is_hidden']


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_confirmed', 'is_active', 'created']
    list_filter = ['is_confirmed', 'is_active']
