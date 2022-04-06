from django import forms

from University_Faculty.accounts.models import Student


class StudentInterestForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('interests', )
        widgets = {
            'interest': forms.CheckboxSelectMultiple(),
        }
