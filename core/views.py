from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


def index(request):
    return render(request, "core/index.html")


@login_required
def secret(request):
    return render(request, "core/secret.html")


class AboutPageView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["section"] = "about"
        return context


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = "core/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["section"] = "profile"
        return context
