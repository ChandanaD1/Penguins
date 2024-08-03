from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    # Specify the forms to use for user creation and change
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    model = CustomUser

    # The fields to be used in displaying the CustomUser model.
    # These are the fields to be displayed on the admin page.
    list_display = ('first_name','last_name', 'username', 'email', 'grade', 'major', 'college', 'status', 'matched')
    list_filter = ('is_staff', 'is_active', 'grade', 'major', 'status', 'matched')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'grade', 'major', 'college', 'financial_situation', 'status', 'matched')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'grade', 'major', 'college', 'financial_situation', 'status'),
        }),
    )
    readonly_fields = ('username',)
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
