from django import forms

class TaskFilterForm(forms.Form):
    search_query = forms.CharField(required=False, label='Поиск')
    status = forms.ChoiceField(choices=[('', 'Любой')] + Task.STATUS_CHOICES, required=False, label='Статус')
    min_priority = forms.IntegerField(required=False, label='Минимальный приоритет')
    max_priority = forms.IntegerField(required=False, label='Максимальный приоритет')
    deadline_before = forms.DateTimeField(required=False, label='Дедлайн до')
    deadline_after = forms.DateTimeField(required=False, label='Дедлайн после')