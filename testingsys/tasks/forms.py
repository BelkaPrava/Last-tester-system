from django import forms
from .models import Task, Collection
from django.forms import ModelForm, TextInput, Textarea
from django.forms.models import (
    inlineformset_factory,
    formset_factory,
    modelform_factory,
    modelformset_factory
)


class CollectionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Название модуля"
        self.fields['description'].label = "Описание модуля"
        self.fields['is_public'].label = "Публичный модуль"

    class Meta:
        model = Collection
        fields = (
            'name',
            'description',
            'is_public'
        )
        widgets = {
            'name': TextInput(attrs={
                'class': 'module-create-form',
                'id': 'task-form-name',
            }),
            'description': Textarea(attrs={
                'class': 'module-create-form-area',
                'id': 'task-form-description'
            }),
        }


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Название задачи"
        self.fields['condition'].label = "Условие задачи"
        self.fields['answer'].label = "Ответ задачи"
    class Meta:
        model = Task
        fields = (
            'name',
            'condition',
            'answer'
        )
        widgets = {
            'name': TextInput(attrs={
                'class': 'task-create-form',
            }),
            'description': Textarea(attrs={
                'class': 'task-create-form-area',
            }),
            'answer': TextInput(attrs={
                'class': 'task-create-form',
            }),
        }