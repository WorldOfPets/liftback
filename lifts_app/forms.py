from django import forms
from lifts_app.models import lift
from lifts_app.models import lift
from lifts_app.models import lift
from lifts_app.models import CustomUser
from lifts_app.models import requests
from lifts_app.models import frequently_used_lifts
from lifts_app.models import CustomUser
from lifts_app.models import CustomUser
from lifts_app.models import status_request
from lifts_app.models import report
from lifts_app.models import lift
from . import models


class frequently_used_liftsForm(forms.ModelForm):
    class Meta:
        model = models.frequently_used_lifts
        fields = [
            "lift",
        ]

    def __init__(self, *args, **kwargs):
        super(frequently_used_liftsForm, self).__init__(*args, **kwargs)
        self.fields["lift"].queryset = lift.objects.all()



class liftForm(forms.ModelForm):
    class Meta:
        model = models.lift
        fields = [
            "vendor_code",
            "is_booked",
            "state",
            "price",
        ]


class lift_imagesForm(forms.ModelForm):
    class Meta:
        model = models.lift_images
        fields = [
            "image",
            "lift",
        ]

    def __init__(self, *args, **kwargs):
        super(lift_imagesForm, self).__init__(*args, **kwargs)
        self.fields["lift"].queryset = lift.objects.all()



class lift_infoForm(forms.ModelForm):
    class Meta:
        model = models.lift_info
        fields = [
            "description",
            "lift",
        ]

    def __init__(self, *args, **kwargs):
        super(lift_infoForm, self).__init__(*args, **kwargs)
        self.fields["lift"].queryset = lift.objects.all()



class reportForm(forms.ModelForm):
    class Meta:
        model = models.report
        fields = [
            "date",
            "sales_amount",
            "expenses",
            "manager",
            "requests",
            "frequently_used_lifts",
        ]

    def __init__(self, *args, **kwargs):
        super(reportForm, self).__init__(*args, **kwargs)
        self.fields["manager"].queryset = CustomUser.objects.all()
        self.fields["requests"].queryset = requests.objects.all()
        self.fields["frequently_used_lifts"].queryset = frequently_used_lifts.objects.all()



class requestsForm(forms.ModelForm):
    class Meta:
        model = models.requests
        fields = [
            "date_closed",
            "price",
            "date_booking",
            "customer",
            "manager",
            "status",
            "reports",
        ]

    def __init__(self, *args, **kwargs):
        super(requestsForm, self).__init__(*args, **kwargs)
        self.fields["customer"].queryset = CustomUser.objects.all()
        self.fields["manager"].queryset = CustomUser.objects.all()
        self.fields["status"].queryset = status_request.objects.all()
        self.fields["reports"].queryset = report.objects.all()



class status_requestForm(forms.ModelForm):
    class Meta:
        model = models.status_request
        fields = [
            "name",
        ]


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = [
            "phone_number",
            "second_name",
            "favorite_lifts",
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields["favorite_lifts"].queryset = lift.objects.all()

