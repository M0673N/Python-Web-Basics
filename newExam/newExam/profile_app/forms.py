from django import forms

from newExam.profile_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['budget', 'first_name', 'last_name', 'profile_image']
        widgets = {'profile_image': forms.FileInput(attrs={'class': 'form-file'})}
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'profile_image': 'Profile Image'}
