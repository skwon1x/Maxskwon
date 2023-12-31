from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

## Класс для формы регистрации пользователя
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # Модель с которой связана создаваемая форма
        model = User
        # Поля которые должны быть видны в форме и в каком порядке
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
