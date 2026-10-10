from django.conf import settings


def site_info(request):
    return {
        "PROJECT_TITLE": settings.PROJECT_TITLE,
        "SITE": settings.SITE,
    }



def debug_csrf_settings(request):
    return {
        'DEBUG_CSRF_TRUSTED_ORIGINS': getattr(settings, 'CSRF_TRUSTED_ORIGINS', []),
        'DEBUG_HTTP_ORIGIN': request.META.get('HTTP_ORIGIN', 'Ingen Origin fundet'),
    }