
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, TemplateView, ListView, UpdateView, DeleteView

from .models import Office


class OfficeCreateView(LoginRequiredMixin, CreateView):
    model = Office
    fields = '__all__'
    
    def get_initial(self):
        return {'org_id':self.args[0]}

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Офис создан")
        return response

    def get_success_url(self):
        return reverse_lazy('organizations:admin', args=[self.args[0]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.args[0]
        return context

class OfficeUpdateView(LoginRequiredMixin, UpdateView):
    model = Office
    fields = '__all__'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Офис успешно изменен")
        return response

    def get_success_url(self):
        return reverse_lazy('organizations:admin', args = [self.object.org_id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = str(self.object.org_id)
        return context
       

class OfficeDeleteView(LoginRequiredMixin, DeleteView):
    model = Office

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Офис удален")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = str(self.object.org_id)
        return context

    def get_success_url(self):
        return reverse_lazy('organizations:admin', args=[self.object.org_id])
