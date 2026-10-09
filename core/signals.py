from django.dispatch import receiver
from allauth.account.signals import email_confirmed
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@receiver(email_confirmed)
def notify_admin_and_lock_user(request, email_address, **kwargs):
    """Sætter brugeren som inaktiv (kræver godkendelse) og adviserer admin, når mailen er bekræftet."""
    new_user = email_address.user
    
    # Lås brugeren nu – de har bekræftet e-mailen, så nu skal admin godkende
    new_user.is_active = False
    new_user.save()
    
    admin_emails = settings.ADMIN_NEW_USER
    if admin_emails:
        subject = _("New user verified email and awaits approval: %(username)s") % {
            "username": new_user.username
        }
        message = _(
            "A new user has verified their email address and is now awaiting your approval.\n\n"
            "Username: %(username)s\n"
            "Email: %(email)s\n\n"
            "Please log in to the admin panel to activate this account."
        ) % {"username": new_user.username, "email": new_user.email}
        
        send_mail(
            subject=str(subject),
            message=str(message),
            from_email=None,
            recipient_list=admin_emails,
            fail_silently=True,
        )


@receiver(pre_save, sender=User)
def notify_user_on_activation(sender, instance, **kwargs):
    """Sender en e-mail til brugeren, når 'is_active' ændres fra False til True."""
    # Hvis brugeren allerede findes i databasen (dvs. det er en opdatering og ikke en oprettelse)
    if instance.pk:
        try:
            old_value = User.objects.get(pk=instance.pk).is_active
            login_url = settings.SITE + reverse("account_login")            # Tjek om status ændres fra False (inaktiv) til True (aktiv)
            if not old_value and instance.is_active:
                subject = _("Your account has been approved!")
                message = _(
                    "Hello %(username)s,\n\n"
                    "An administrator has approved your account. You can now log in here:\n\n"
                    "%(login_url)s\n\n"
                    "Best regards,\n"
                    "The Team"
                ) % {"username": instance.username, "login_url": login_url}
                
                send_mail(
                    subject=str(subject),
                    message=str(message),
                    from_email=None,  # Bruger DEFAULT_FROM_EMAIL
                    recipient_list=[instance.email],
                    fail_silently=True,
                )
        except User.DoesNotExist:
            pass
