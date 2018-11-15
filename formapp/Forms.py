from django import  forms
from formapp.models import User


class NewUserforms(forms.ModelForm):
    class Meta():
        model = User
        fields = "__all__"


