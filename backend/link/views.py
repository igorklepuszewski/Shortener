from link.forms import LinkForm
from django.http.response import Http404, HttpResponseRedirect
from link.models import Link
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
# Create your views here.


def redirect_url(request, short_hash):
    try:
        link = Link.objects.get(_short_hash=short_hash)
        return HttpResponseRedirect(link.long_url)
    except ObjectDoesNotExist:
        raise Http404('Link broken')


def home_view(request):

    template = 'home.html'
    context = {}
    context['form'] = LinkForm()
    if request.method == "GET":
        context['short_url'] = None
        return render(request, template, context)

    if request.method == "POST":
        form = LinkForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data["long_url"])
            # if given long_url exists in database
            # i want to return to user short_url that is
            # already in database
            if Link.objects.filter(
                long_url=form.cleaned_data["long_url"]
                    ).exists():
                link = Link.objects.get(long_url=form.cleaned_data["long_url"])
            else:
                link = form.save()

            # building link for user, because in database we only store slug
            short_url = request.build_absolute_uri("/") + link.short_url
            long_url = link.long_url

            context['short_url'] = short_url
            context['long_url'] = long_url

            return render(request, template, context)

        # if form is not valid return form with form.errors
        context['short_url'] = None
        context['form'] = form

        return render(request, template, context)
