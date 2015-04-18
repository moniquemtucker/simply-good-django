__author__ = 'Monique Tucker'

from django import forms
from .models import DiaryEntry


class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ('entry_date', 'whole_foods', 'processed_foods', 'notes')

    def __init__(self, *args, **kwargs):
        super(DiaryEntryForm, self).__init__(*args, **kwargs)
        self.fields.get('entry_date').widget = forms.TextInput(
            attrs={'placeholder': 'YYYY-MM-DD'})

    # def save(self, commit=True):
    #     diaryentry = super(DiaryEntryForm, self).save(commit=False)
    #     diaryentry.entry_date = self.cleaned_data['entry_date']
    #     diaryentry.whole_foods = self.cleaned_data['whole_foods']
    #     diaryentry.processed_foods = self.cleaned_data['processed_foods']
    #     diaryentry.notes = self.cleaned_data['notes']
    #
    #     if commit:
    #         diaryentry.save()
    #
    #         return diaryentry