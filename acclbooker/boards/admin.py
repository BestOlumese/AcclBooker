from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin):
    exclude = ('user',)

    # Automatically set the `user` field to the current user on creation
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created (not edited)
            obj.user = request.user
        super().save_model(request, obj, form, change)

    # Automatically set the `user` field to the current user
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created (not edited)
            obj.user = request.user
        super().save_model(request, obj, form, change)

    # Only allow deletion if the current user is the creator
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:  # Admins can delete any object
            return True
        if obj is not None and obj.user != request.user:
            return False
        return super().has_delete_permission(request, obj)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    
    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return super().has_change_permission(request, obj)
    
    list_display = ('title', 'is_completed', 'begins', 'ends')

admin.site.register(Board, BoardAdmin)