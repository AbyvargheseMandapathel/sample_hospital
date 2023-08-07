from django import forms

from visitors.models import Department, Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('name', 'mobile_number', 'doctor','department')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].choices = [(department.id, department.name) for department in Department.objects.all()]

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data['mobile_number']
        if not mobile_number.isdigit():
            raise forms.ValidationError('Mobile number must be a numeric value.')
        return mobile_number

