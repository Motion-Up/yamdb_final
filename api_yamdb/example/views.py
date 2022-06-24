from django.views.generic import DetailView, ListView
from django.shortcuts import render
from reviews.models import Title


class TitlesList(DetailView):
    model = Title
    template_name = 'detail.html'


class TitlesListView(ListView):
    model = Title
    template_name = 'list.html'
    context_object_name = 'titles'


def index(request):
    context = {
        'titles': Title.objects.all()
    }
    return render(request, 'base.html', context)
