from accounts.models import Role
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class RoleIndexView(ListView):
    template_name = 'role/list.html'
    model = Role
    context_object_name = 'roles'
    paginate_by = 4
    paginate_orphans = 0
    page_kwarg = 'page'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context


class RoleCreateView(CreateView):
    model = Role
    template_name = 'add.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('accounts:roles_list')


class RoleUpdateView(UpdateView):
    model = Role
    template_name = 'change.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('accounts:roles_list')


class RoleDeleteView(DeleteView):
    model = Role
    template_name = 'delete.html'
    success_url = reverse_lazy('accounts:roles_list')