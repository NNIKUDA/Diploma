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


def validate_name(value):
    if not value.isalpha():
        raise ValidationError('This field must contain only letters')
    return value


class ProfileForm(forms.Form):
    new_email = forms.EmailField(max_length=254, required=False)
    username = forms.CharField(max_length=150, required=False)
    first_name = forms.CharField(max_length=150, validators=[validate_name], required=False)
    last_name = forms.CharField(max_length=150, validators=[validate_name], required=False)
    email = forms.EmailField(max_length=254)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = HiddenInput()

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def _post_clean(self):
        """Reject usernames that differ only in case."""
        user = get_user_model().objects.get(email=self.cleaned_data['email'])
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("new_email")
        if user.username != username:
            if (
                    get_user_model().objects.filter(username__iexact=username).exists()
            ):
                self.add_error("username", "This name already exist")

        if user.email != email:
            if (
                    get_user_model().objects.filter(email__iexact=email).exists()
            ):
                self.add_error("new_email", "This email already exist")

    def save(self, commit=True):
        # user = super().save(commit=False)
        user = get_user_model().objects.get(email=self.cleaned_data['email'])
        if user.username != self.cleaned_data['username']:
            user.username = self.cleaned_data['username']
        if user.email != self.cleaned_data['new_email']:
            user.email = self.cleaned_data['new_email']

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class MyPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class MySetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
