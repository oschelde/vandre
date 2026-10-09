from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
from django import forms


class CustomSignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"placeholder": _("First Name")})
    )

    last_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"placeholder": _("Last Name")})
    )

    phone = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": _("Phone")}),
    )

    def signup(self, request, user):
        """
        Called after the user has been created, allowing you to save additional inforxmation.
        """

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.phone = self.cleaned_data["phone"]
        user.save()
