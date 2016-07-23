from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import User, StripeAccount, StripeEvent


class CodesyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class CodesyUserAdmin(UserAdmin):
    form = CodesyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        ('Stripe tokens', {'fields': ('stripe_customer','stripe_bank_account')}),
    )

admin.site.register(User, CodesyUserAdmin)
admin.site.register(StripeAccount)
admin.site.register(StripeEvent)
