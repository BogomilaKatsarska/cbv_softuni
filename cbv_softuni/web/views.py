import random
from django import views, forms
from django.http import HttpResponse
from django.views import generic as views

from django.shortcuts import render

from cbv_softuni.web.models import Employee


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            )
        }
# class IndexView:
#     def __init__(self):
#         self.values = [random.randint(1, 15)]
#
#     @classmethod
#     def get_view(cls):
#         return cls().view
#
#     def view(self, request):
#         return HttpResponse(f'It works: {self.values}')
#
#
# def view(request):
#     return HttpResponse('It works')

# index_view = IndexView().get_view
# class IndexView(views.View):
#     def get(self, request):
#         return HttpResponse('It works from CBV')
#
#     def post(self, request):
#         pass

# class IndexViewWithProfile(IndexView):
#     def __init__(self):
#         super().__init__()
#         self.values.append(random.randint(15, 30))


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'Bare view',
        }
        return render(request, 'index.html', context)


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': 'Template view', #static context
    }
    #dynamic context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context


class IndexViewWithList(views.ListView):
    model = Employee
    template_name = 'index.html'
    #object_list == employees. Below renames 'object_list' to 'employees'
    context_object_name = 'employees'
    extra_context = {
        'title': 'List view',  # static context
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-first_name')
        return queryset


class EmployeeDetailsView(views.DetailView):
    context_object_name = 'employee'
    model = Employee
    template_name = 'employees/details.html'


class EmployeeCreateView(views.CreateView):
    template_name = 'employees/create.html'
    model = Employee
    # fields = '__all__'

    form_class = EmployeeCreateForm()

    #we use below for debug
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)
