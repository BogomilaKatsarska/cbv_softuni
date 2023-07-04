from django.urls import path
from django.views import generic as views
from cbv_softuni.web.views import IndexViewWithList, EmployeeDetailsView, EmployeeCreateView, EmployeeUpdateView

# IndexViewWithProfile

urlpatterns = (
    path('', IndexViewWithList.as_view(), name='index'),
    path('details/<int:pk>/', EmployeeDetailsView.as_view, name='employee details'),
    path('redirect-to-index/', views.RedirectView.as_view(url='/'), name='redirect'),
    path('create/', EmployeeCreateView.as_view(), name='employee create'),
    path('update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee update'),
    # path('withprofile/', IndexViewWithProfile.get_view()),
)