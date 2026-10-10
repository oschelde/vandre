from django.conf import settings


def site_info(request):
    return {
        "PROJECT_TITLE": settings.PROJECT_TITLE,
        "SITE": settings.SITE,
        'ALLOWED_HOSTS': settings.ALLOWED_HOSTS,
        'CSRF_TRUSTED_ORIGINS': settings.CSRF_TRUSTED_ORIGINS,
        'HTTP_ORIGIN': request.META.get('HTTP_ORIGIN', 'Ingen Origin fundet'),
    }