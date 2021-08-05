from django.forms import ModelForm

from apps.team.models.player import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = [
            'team',
            'name',
            'dni',
        ]
