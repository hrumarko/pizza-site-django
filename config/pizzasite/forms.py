from django import forms


class DeliveryForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': '*Имя', 'class': 'delivery-name'}))
    number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': '*Номер','class': 'delivery-number'}))
    address = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Улица, номер дома, номер квартиры','class': 'delivery-address', 'rows': '4',}))
    commentary = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
            'rows': 7,
            'placeholder': 'Комментарий к заказу',
            'class': 'delivery-commentary',
            }
        ))
