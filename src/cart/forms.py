from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
    additional_notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}))
