from django.forms import ModelForm
from dest.models import Subscriber

class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'