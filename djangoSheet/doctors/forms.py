from django.forms import ModelForm
from doctors.models import Doctors


class DoctorForm(ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'
