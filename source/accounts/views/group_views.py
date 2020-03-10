from django.db.models import ProtectedError

from accounts.forms import GroupForm, StudentAddStudyGroupForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from accounts.models import StudyGroup, User, Profile, AdminPosition
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect

class GroupListView(PermissionRequiredMixin, ListView):
    template_name = 'group/list.html'
    model = StudyGroup
    ordering = ["-name"]
    context_object_name = 'group_list'
    paginate_by = 10
    paginate_orphans = 2
    permission_required = "accounts.view_group"
    permission_denied_message = "Доступ запрещен"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context


class GroupDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'group/detail.html'
    model = StudyGroup
    context_object_name = 'group'
    permission_required = "accounts.view_group"
    permission_denied_message = "Доступ запрещен"


class GroupCreateView(CreateView):
    model = StudyGroup
    template_name = 'add.html'
    # permission_required = "accounts.add_group"
    # permission_denied_message = "Доступ запрещен"
    form_class = GroupForm
    context_object_name = 'group'

    def form_valid(self, form):
        self.text = form.cleaned_data['name']
        if StudyGroup.objects.filter(name=self.text.capitalize()):
            messages.error(self.request, 'Объект с таким названием уже существует!')
            return render(self.request, 'add.html', {})
        else:
            self.create_group(form)
        return self.get_success_url()

    def create_group(self, form):
        group = StudyGroup(name=self.text.capitalize(),
                           group_leader=form.cleaned_data['group_leader'],
                           head_teaher=form.cleaned_data['head_teacher'],
                           started_at=form.cleaned_data['started_at'])
        students = form.cleaned_data['students']
        group.save()
        self.set_position_head_teacher(group)
        self.set_position_group_leader(group)
        group.students.set(students)
        return group

    def set_position_head_teacher(self, obj):
        profile_tc = Profile.objects.get(user=User.objects.get(id=obj.head_teaher.pk))
        profile_tc.admin_position = AdminPosition.objects.get(name='Куратор')
        return profile_tc.save()

    def set_position_group_leader(self, obj):
        profile_st = Profile.objects.get(user=User.objects.get(id=obj.group_leader.pk))
        profile_st.admin_position = AdminPosition.objects.get(name='Староста')
        return profile_st.save()

    def get_success_url(self):
        return redirect('accounts:groups')



class GroupUpdateView(UpdateView):
    model = StudyGroup
    template_name = 'change.html'
    form_class = GroupForm
    # permission_required = "accounts.change_group"
    # permission_denied_message = "Доступ запрещен"

    def get_success_url(self):
        return reverse('accounts:groups')


class GroupDeleteView(PermissionRequiredMixin, DeleteView):
    model = StudyGroup
    template_name = 'delete.html'
    success_url = reverse_lazy('accounts:groups')
    permission_required = "accounts.delete_group"
    permission_denied_message = "Доступ запрещен"

    def get(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'error.html')


class GroupStudentAdd(UpdateView):
    model = StudyGroup
    template_name = 'group/group_student_add.html'
    form_class = StudentAddStudyGroupForm
    permission_required = "accounts.change_group"
    permission_denied_message = "Доступ запрещен"

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.filter(pk=self.kwargs['pk'])
        groups = StudyGroup.objects.all()
        context.update({
            'user': user,
            'groups': groups,
        })
        return context

    def form_valid(self, form):
        self.student_pk = self.kwargs['pk']
        text = form.cleaned_data['group_name']
        # user = User.objects.filter(pk=self.kwargs['pk'])
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        group_name = get_object_or_404(StudyGroup, name=text)
        group_name.students.add(user.pk)
        group_name.save()
        return self.get_success_url()

    def get_success_url(self):
        return redirect('accounts:user_detail', pk=self.student_pk)
        # return redirect('accounts:groups')


