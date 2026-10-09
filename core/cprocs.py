from django.conf import settings


def site_info(request):
    return {
        "PROJECT_TITLE": settings.PROJECT_TITLE,
        "SITE": settings.SITE,
    }
