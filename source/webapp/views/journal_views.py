from webapp.models import Journal
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class JournalIndexView(ListView):
    template_name = 'progress/list.html'
    model = Journal
    context_object_name = 'journals'
    paginate_by = 30
    paginate_orphans = 0
    page_kwarg = 'page'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context


class JournalCreateView(CreateView):
    model = Journal
    template_name = 'add.html'
    fields = ['student', 'date', 'discipline', 'theme', 'grade']

    def get_success_url(self):
        return reverse('webapp:journal')


class JournalUpdateView(UpdateView):
    model = Journal
    template_name = 'change.html'
    fields = ['grade']

    def get_success_url(self):
        return reverse('webapp:journal')


class JournalDeleteView(DeleteView):
    model = Journal
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:journal')

