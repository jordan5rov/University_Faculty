from django import forms

from University_Faculty.common.helpers import BootstrapFormMixin
from University_Faculty.web.models import News, Event


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


class CreateEventForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        event = super().save(commit=False)
        if commit:
            event.save()

        return event

    class Meta:
        model = Event
        fields = ('title', 'image', 'description', 'date')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Event title',
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Event description'
                }
            ),
            'date': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Enter Event date',
                    'type': 'datetime-local'
                }
            )
            # 'date': forms.DateField(
            #     attrs={
            #         'placeholder': 'Enter Event date',
            #         'class': 'form-control datetimepicker-input',
            #
            #     }
            # )
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


class EditEventForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Event
        fields = ('title', 'image', 'description', 'date')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter News title',
                }),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Enter News description'
                }
            ),
            'date': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Enter Event date',
                    'type': 'datetime-local'
                }
            ),
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


class DeleteEventForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Event
        fields = ()
