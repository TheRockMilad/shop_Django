from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.core import validators
from .models import Post


class InputForm0(forms.Form):
    name = forms.CharField(max_length=10, required=True, label="نام")
    family = forms.CharField(max_length=15, label="نام خانوادگی")
    age = forms.IntegerField(label="سن", label_suffix="=>")
    is_active = forms.BooleanField(initial=True)


# ------------------------------------------------------------------------------

class InputForm2(forms.Form):
    name = forms.CharField(max_length=10, required=True, label="نام")
    family = forms.CharField(max_length=15, label="نام خانوادگی")
    age = forms.IntegerField(label="سن", label_suffix="=>")
    is_active = forms.BooleanField(initial=True, label="فعال/غیرفعال")
    avg = forms.DecimalField(max_digits=2, decimal_places=2, label="معدل")
    email = forms.EmailField(max_length=30, label="ایمیل")
    register_date = forms.DateField(label="تاریخ تولد")
    url = forms.URLField(label="آدرس سایت", required=False, initial="http://")
    image = forms.ImageField(label="تصویر", required=False)
    FAVORITS_COLOR = [
        ("1", "RED"),
        ("2", "Blue"),
        ("3", "Green"),
        ("4", "Gray"),
        ("5", "Black")
    ]
    color = forms.ChoiceField(choices=FAVORITS_COLOR, label="رنگ مورد علاقه")


# ------------------------------------------------------------------------------
class InputForm3(forms.Form):
    name = forms.CharField(
        max_length=10,
        required=True,
        label="نام ",
        widget=forms.TextInput(attrs={"class": "c1", "placeholder": "نام را وارد کنید"}))
    family = forms.CharField(
        max_length=15,
        label="نام خانوادگی",
        widget=forms.TextInput(attrs={"class": "c1", "placeholder": "نام خانوادگی را وارد کنید"}))
    password = forms.CharField(
        max_length=100,
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={"class": "c1", "placeholder": "رمز را وارد کنید"}))
    Year_Choies = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", ]
    register_date1 = forms.DateField(label="تاریخ تولد", widget=forms.SelectDateWidget(years=Year_Choies))
    register_date2 = forms.DateField(label="تاریخ تولد", initial=datetime.date.today,
                                     widget=forms.NumberInput(attrs={'type': 'date'}))
    FAVORITS_COLOR = [
        ("1", "RED"),
        ("2", "Blue"),
        ("3", "Green"),
        ("4", "Gray"),
        ("5", "Black")
    ]
    colors1 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITS_COLOR)
    colors2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITS_COLOR)
    description = forms.BooleanField(widget=forms.Textarea)
    description.widget.attrs.update({"class": "c1"})


# ------------------------------------------------------------------------------
def checkValidateName(value):
    value = str(value)
    if len(value) < 3 or len(value) > 8:
        raise forms.ValidationError("اسم درست نیست")


# def checkValidateage(value):
#     value = int(value)
#     if value<20 or value>40:
#         raise forms.ValidationError("خارج از رده انتخاب شده")


class InputForm4(forms.Form):
    name = forms.CharField(max_length=10, required=True, label="نام", validators=[checkValidateName])
    family = forms.CharField(max_length=15, label="نام خانوادگی")
    age = forms.IntegerField(label="سن",
                             validators=[validators.MaxValueValidator(40, message="سن نیمتواند بیشتر از 40 باشد"),
                                         validators.MinValueValidator(20, message="سن نمیتواند کمتر از 20 باشد")])
    is_active = forms.BooleanField(initial=True, label='فعال/غیرفعال')
    #
    # def clean_name(self):
    #     name = self.cleaned_data["name"]
    #     return name

    # def clean_family(self):
    #     family = self.cleaned_data["family"]
    #     if family[0] != 'A':
    #         raise ValidationError("نام خانوادگی با A شروع نشده است ")
    #     return family
    #
    # def clean_age(self):
    #     age = self.cleaned_data["age"]
    #     return age


class InputForm6(forms.Form):
    name = forms.CharField(max_length=30, label="نام")
    age = forms.IntegerField(label="سن")

    def clean_age(self):
        name = self.cleaned_data["name"]
        if name[0] != 'A':
            raise ValidationError("نام خانوادگی با A شروع نشده است ")
        return name


class InputForm7(forms.ModelForm):
    class Meta :
        model = Post
        fields = "__all__"

