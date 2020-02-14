from django.urls import reverse_lazy
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView
from django.views.generic import TemplateView
from .forms import ParentForm
from .models import Parent, Child1, Child2, Child3


class Child1Inline(InlineFormSetFactory):
    model = Child1
    fields = '__all__'



class Child2Inline(InlineFormSetFactory):
    model = Child2
    fields = '__all__'


class Child3Inline(InlineFormSetFactory):
    model = Child3
    fields = '__all__'


class ParentCreateView(CreateWithInlinesView):
    model = Parent
    fields = ['name']
    context_object_name = 'parent'
    inlines = [Child1Inline, Child2Inline, Child3Inline]
    template_name = 'extraviews_test/parent.html'
    success_url = reverse_lazy('extraviews_test:success')


class ParentUpdateView(UpdateWithInlinesView):
    model = Parent
    form_class = ParentForm
    inlines = [Child1Inline, Child2Inline, Child3Inline]
    template_name = 'extraviews_test/parent.html'
    success_url = reverse_lazy('extraviews_test:success')

class SuccessView(TemplateView):
    template_name = "extraviews_test/success.html"