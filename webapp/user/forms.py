from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm, PasswordChangeForm
from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError
from django.forms import HiddenInput


class SingUpForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())
    register_policy = forms.BooleanField()

    class Meta:
        fields = ['email', 'password']
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['register_policy'].widget.attrs['class'] = 'custom-control-input'

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data['password']
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password', error)

    def save(self, commit=True):
        UserModel = get_user_model()
        user = UserModel.objects.create_user(email=self.cleaned_data['email'], password=self.cleaned_data['password'])
        user.save()
        return user


class SingInForm(forms.Form):
    email = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())
    remember_box = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['remember_box'].widget.attrs['class'] = 'custom-control-input'

    class Meta:
        fields = '__all__'
        # model = User

