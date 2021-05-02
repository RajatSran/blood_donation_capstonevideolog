from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('fullname','contact','pat_code','wardno','age','gender','Admit_Status','facility','address','admitdate','patientimg')
        labels = {
            'fullname':'Patient Name',
            'contact':'Contact Number',
            'pat_code':'Patient Id',
            'age':'Age',
            'gender':'Gender',
            'Admit_Status':'Admit Status',
            'facility':'Facilities',
            'address':'Address',
            'admitdate':'Admit Date',
            'wardno':'Ward No',
            'patientimg':'Patient Image'
        }

        widgets = {
        'admitdate': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date','required':True}),
        'address': forms.Textarea(attrs={'rows': 3, 'cols': 20}),
        'patientimg': forms.FileInput()
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm,self).__init__(*args, **kwargs)
        self.fields['pat_code'].required = False
