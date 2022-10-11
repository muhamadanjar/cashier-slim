from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin

from cashier.backoffice.mixins import ContextTitleMixin


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        context['heading'] = "Dashboard"
        context['pageview'] = "Dashboards"
        return render(request, 'backoffice/dashboard.html', context)


@method_decorator(login_required, name='dispatch')
class BaseListView(ContextTitleMixin, ListView):
    model = None
    title_page = 'List'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(name__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        page_number = self.request.GET.get('page', 1)
        context = super().get_context_data(**kwargs)
        page_range = context['page_obj'].paginator.get_elided_page_range(number=page_number)
        context['page_range'] = page_range
        return context


class BaseFormView(FormMixin, DetailView):
    template_name = "backoffice/form.html"
    success_url = "/backoffice"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = self.get_object()
        if form.is_valid():
            form.save()
            messages.success(self.request, f'Successfully {self.title_page}')
            return self.form_valid(form)
        else:
            messages.error(self.request, 'Something wrong')
            return self.form_invalid(form)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(instance=self.get_object() or None, **self.get_form_kwargs())


@method_decorator(login_required, name='dispatch')
class BaseDeleteView(DetailView):
    model = None

    def dispatch(self, request, *args, **kwargs):
        # handle if user not same
        instance = self.get_object()
        if instance.created_by != request.user:
            messages.warning(request, "You can't delete this. You don't have permission")
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        messages.success(self.request, 'Successfully deleted one survey')
        return redirect("backoffice:plant:index")


@method_decorator(login_required, name='dispatch')
class BaseCreateFormView(CreateView):
    template_name = "backoffice/form.html"
    success_url = "/backoffice"


@method_decorator(login_required, name='dispatch')
class BaseDetailView(ContextTitleMixin, DetailView):
    model = None
    template_name = "backoffice/detail.html"
    title_page = "Detail"


class PagesLoginView(View):
    def get(self, request):
        return render(request, 'backoffice/login.html')
