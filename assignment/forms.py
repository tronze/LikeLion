from django import forms
from .models import AssignmentComment, AssignmentSubmitTotal


# Create your forms here.


class AssignmentCommentForm(forms.ModelForm):
    submit = forms.IntegerField(
        required=True,
        widget=forms.HiddenInput()
    )
    content = forms.CharField(
        label='댓글달기',
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control comment-content',
                'placeholder': '댓글',
                'required': 'True',
                'rows': 5,
            }
        )
    )

    class Meta:
        model = AssignmentComment
        fields = ('submit', 'content')

    def clean(self):
        cleaned = super().clean()
        cleaned['submit'] = AssignmentSubmitTotal.objects.get(pk=cleaned['submit'])
        return cleaned
