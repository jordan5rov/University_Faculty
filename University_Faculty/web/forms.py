from django import forms

from University_Faculty.common.helpers import BootstrapFormMixin
from University_Faculty.web.models import News


class CreateNewsForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        news = super().save(commit=False)
        if commit:
            news.save()

        return news

    class Meta:
        model = News
        fields = ('title', 'image', 'description')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter News title',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Enter News description'
                }
            )
        }


class EditNewsForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = News
        fields = ('title', 'image', 'description')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter News title',
                }),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Enter News description'
                }
            )
        }


class DeleteNewsForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = News
        fields = ()
