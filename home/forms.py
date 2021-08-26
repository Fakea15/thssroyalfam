from django import forms
from.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        labels = {
            "hming": '',
            "comment": '',
        }
        widgets = {
            'hming': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'I hming ziak rawh le'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Database a hmuh tur'}),
        }

