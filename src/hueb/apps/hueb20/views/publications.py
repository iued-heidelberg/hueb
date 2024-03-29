# flake8: noqa
import os
import re

import requests
from django import forms
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import FormView
from hueb import settings
from hueb.apps.publications.models import Publication


class FormListView(ListView, FormView):
    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        # From BaseListView
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(
                _("Empty list and '%(class_name)s.allow_empty' is False.")
                % {"class_name": self.__class__.__name__}
            )

        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.get(request, *args, **kwargs)


class SubscribeForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        pattern = re.compile(r"[A-Z][a-z]*\s[A-Z][a-z]*")
        if name != "" and not pattern.match(name):
            msg = _(
                "Please write your name if form 'Firstname Lastname' or leave empty for anonymous subscription"
            )
            self.add_error("name", msg)
        return cleaned_data


class Publications(FormListView):
    # specify the model to use
    template_name = "hueb20/publications/publications.html"
    model = Publication
    paginate_by = 3
    form_class = SubscribeForm
    # success_url = reverse_lazy("publications")

    def download_pdf(request, pk):
        pub = Publication.objects.get(id=pk)
        with open(os.path.join(settings.MEDIA_ROOT, pub.file.path), "rb") as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response["Content-Disposition"] = "attachment; filename=invoice.pdf"
            return response
        # response = requests.get(pub.file.url)
        # response = HttpResponse(response.content, content_type='application/pdf')
        # return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get("sub", None) == "sub":
            context["successful_subscribed"] = True
        elif self.kwargs.get("sub", None) == "unsub":
            context["successful_unsubscribed"] = True
        context["recent"] = (
            Publication.objects.all().order_by("-publication_date").first()
        )
        if self.request.method == "POST":
            form = self.form_class(data=self.request.POST)
        else:
            form = self.form_class()
        context["subscribe_form"] = form
        return context

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        url = "https://listserv.uni-heidelberg.de/cgi-bin/wa"
        if name == "":
            name = "Anonymous"
        if "sub" in self.request.POST:
            r = requests.get(
                "https://listserv.uni-heidelberg.de/cgi-bin/wa",
                params={
                    "SUBED2": "HUEB-NEWSLETTER-IUED",
                    "A": 1,
                    "L": "HUEB-NEWSLETTER-IUED",
                    "p": name,
                    "s": email,
                    "b": "Subscribe",
                    "_charset_": "UTF-8",
                },
            )

            url = reverse("publicationsSub", kwargs={"sub": "sub"})
            return HttpResponseRedirect(url)
        elif "unsub" in self.request.POST:
            r = requests.get(
                "https://listserv.uni-heidelberg.de/cgi-bin/wa",
                params={
                    "SUBED2": "HUEB-NEWSLETTER-IUED",
                    "A": 1,
                    "L": "HUEB-NEWSLETTER-IUED",
                    "p": name,
                    "q": name,
                    "s": email,
                    "t": email,
                    "a": "Unsubscribe",
                    "_charset_": "UTF-8",
                },
            )

            url = reverse("publicationsSub", kwargs={"sub": "unsub"})
            return HttpResponseRedirect(url)
        return super().form_valid(form)

        # return HttpResponseRedirect(reverse_lazy("publications"))

    def get_queryset(self):
        return Publication.objects.all().order_by("-publication_date").all()
