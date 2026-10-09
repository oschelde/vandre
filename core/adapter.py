from allauth.core.exceptions import ImmediateHttpResponse
from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class ApprovalAccountAdapter(DefaultAccountAdapter):
    def pre_login(self, request, user, *args, **kwargs):
        # 1. Tjek om brugeren overhovedet har bekræftet sin e-mail endnu
        # (Hvis ACCOUNT_EMAIL_VERIFICATION = "mandatory", håndterer allauth det meste,
        # men dette sikrer, at de ikke logger ind før bekræftelse)
        
        # 2. Hvis e-mailen ER bekræftet, men admin ikke har aktiveret dem (is_active)
        if not user.is_active:
            messages.warning(
                request,
                _("Your email is verified, but your account is awaiting administrator approval. An email will be sent to you, when you can login.")
            )
            raise ImmediateHttpResponse(redirect("account_login"))
            
        super().pre_login(request, user, *args, **kwargs)
