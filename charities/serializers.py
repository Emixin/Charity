from rest_framework import serializers

from .models import Benefactor
from .models import Charity, Task


class BenefactorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Benefactor
        fields = (
            'user',
            'experience',
            'free_time_per_week',
        )

    def save(self, **kwargs):
        """
        kwargs should contain `user` object
        it should be evaluated from AuthToken
        """
        user = kwargs.get('user')
        assert user is not None, "`user` is None"
        return super().save(user=user)


class CharitySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Charity
        fields = (
            'user',
            'name',
            'reg_number',
        )

    def save(self, **kwargs):
        """
        kwargs should contain `user` object
        it should be evaluated from AuthToken
        """
        user = kwargs.get('user')
        assert user is not None, "`user` is None"
        return super().save(user=user)


class TaskSerializer(serializers.ModelSerializer):
    TASK_STATUS_CHOICES = [
        ('O', 'Open'),
        ('I', 'In Progress'),
        ('D', 'Done'),
        ('C', 'Closed'),
    ]

    state = serializers.ChoiceField(read_only=True, choices=TASK_STATUS_CHOICES)
    assigned_benefactor = BenefactorSerializer(required=False)
    charity = CharitySerializer(read_only=True)
    charity_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Charity.objects.all(), source='charity')

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'state',
            'charity',
            'charity_id',
            'description',
            'assigned_benefactor',
            'date',
            'age_limit_from',
            'age_limit_to',
            'gender_limit',
        )

