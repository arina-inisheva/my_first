from django.forms import ModelForm, TextInput, Textarea, NumberInput, CheckboxInput, FileInput

from app_advertisment.models import Advertisement


class DBAdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'price': 'Цена',
            'auction': 'Возможность торга',
            'image' : 'Изображение'

        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': Textarea(attrs={'class': 'form-control form-control-lg'}),
            'price': NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': FileInput(attrs={'class': 'form-control form-control-lg'})

        }
# title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), label='Заголовок')
    # description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}), label='Описание')
    # price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
    #                            min_value=0, label='Цена')
    #
    # auction = forms.BooleanField(widget=forms.CheckboxInput(
    #     attrs={'class': 'form-check-input'}), required=False,
    #     label='Возможность торга'
    # )
    # image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}), label='Изображение', required=False)