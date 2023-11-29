from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class frequently_used_liftsListView(generic.ListView):
    model = models.frequently_used_lifts
    form_class = forms.frequently_used_liftsForm


class frequently_used_liftsCreateView(generic.CreateView):
    model = models.frequently_used_lifts
    form_class = forms.frequently_used_liftsForm


class frequently_used_liftsDetailView(generic.DetailView):
    model = models.frequently_used_lifts
    form_class = forms.frequently_used_liftsForm


class frequently_used_liftsUpdateView(generic.UpdateView):
    model = models.frequently_used_lifts
    form_class = forms.frequently_used_liftsForm
    pk_url_kwarg = "pk"


class frequently_used_liftsDeleteView(generic.DeleteView):
    model = models.frequently_used_lifts
    success_url = reverse_lazy("lifts_app_frequently_used_lifts_list")


class liftListView(generic.ListView):
    model = models.lift
    form_class = forms.liftForm


class liftCreateView(generic.CreateView):
    model = models.lift
    form_class = forms.liftForm


class liftDetailView(generic.DetailView):
    model = models.lift
    form_class = forms.liftForm


class liftUpdateView(generic.UpdateView):
    model = models.lift
    form_class = forms.liftForm
    pk_url_kwarg = "pk"


class liftDeleteView(generic.DeleteView):
    model = models.lift
    success_url = reverse_lazy("lifts_app_lift_list")


class lift_imagesListView(generic.ListView):
    model = models.lift_images
    form_class = forms.lift_imagesForm


class lift_imagesCreateView(generic.CreateView):
    model = models.lift_images
    form_class = forms.lift_imagesForm


class lift_imagesDetailView(generic.DetailView):
    model = models.lift_images
    form_class = forms.lift_imagesForm


class lift_imagesUpdateView(generic.UpdateView):
    model = models.lift_images
    form_class = forms.lift_imagesForm
    pk_url_kwarg = "pk"


class lift_imagesDeleteView(generic.DeleteView):
    model = models.lift_images
    success_url = reverse_lazy("lifts_app_lift_images_list")


class lift_infoListView(generic.ListView):
    model = models.lift_info
    form_class = forms.lift_infoForm


class lift_infoCreateView(generic.CreateView):
    model = models.lift_info
    form_class = forms.lift_infoForm


class lift_infoDetailView(generic.DetailView):
    model = models.lift_info
    form_class = forms.lift_infoForm


class lift_infoUpdateView(generic.UpdateView):
    model = models.lift_info
    form_class = forms.lift_infoForm
    pk_url_kwarg = "pk"


class lift_infoDeleteView(generic.DeleteView):
    model = models.lift_info
    success_url = reverse_lazy("lifts_app_lift_info_list")


class reportListView(generic.ListView):
    model = models.report
    form_class = forms.reportForm


class reportCreateView(generic.CreateView):
    model = models.report
    form_class = forms.reportForm


class reportDetailView(generic.DetailView):
    model = models.report
    form_class = forms.reportForm


class reportUpdateView(generic.UpdateView):
    model = models.report
    form_class = forms.reportForm
    pk_url_kwarg = "pk"


class reportDeleteView(generic.DeleteView):
    model = models.report
    success_url = reverse_lazy("lifts_app_report_list")


class requestsListView(generic.ListView):
    model = models.requests
    form_class = forms.requestsForm


class requestsCreateView(generic.CreateView):
    model = models.requests
    form_class = forms.requestsForm


class requestsDetailView(generic.DetailView):
    model = models.requests
    form_class = forms.requestsForm


class requestsUpdateView(generic.UpdateView):
    model = models.requests
    form_class = forms.requestsForm
    pk_url_kwarg = "pk"


class requestsDeleteView(generic.DeleteView):
    model = models.requests
    success_url = reverse_lazy("lifts_app_requests_list")


class status_requestListView(generic.ListView):
    model = models.status_request
    form_class = forms.status_requestForm


class status_requestCreateView(generic.CreateView):
    model = models.status_request
    form_class = forms.status_requestForm


class status_requestDetailView(generic.DetailView):
    model = models.status_request
    form_class = forms.status_requestForm


class status_requestUpdateView(generic.UpdateView):
    model = models.status_request
    form_class = forms.status_requestForm
    pk_url_kwarg = "pk"


class status_requestDeleteView(generic.DeleteView):
    model = models.status_request
    success_url = reverse_lazy("lifts_app_status_request_list")


class CustomUserListView(generic.ListView):
    model = models.CustomUser
    form_class = forms.CustomUserForm


class CustomUserCreateView(generic.CreateView):
    model = models.CustomUser
    form_class = forms.CustomUserForm


class CustomUserDetailView(generic.DetailView):
    model = models.CustomUser
    form_class = forms.CustomUserForm


class CustomUserUpdateView(generic.UpdateView):
    model = models.CustomUser
    form_class = forms.CustomUserForm
    pk_url_kwarg = "pk"


class CustomUserDeleteView(generic.DeleteView):
    model = models.CustomUser
    success_url = reverse_lazy("lifts_app_CustomUser_list")
