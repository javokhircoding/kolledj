from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    description = serializers.CharField(source='context', allow_blank=True, required=False)
    url = serializers.HyperlinkedIdentityField(
        view_name='task-update',
        lookup_field = 'slug',
    )
    delete_url = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'done',
            'url',
            'delete_url',
        ]

    def get_delete_url(self, obj):
        request = self.context.get('request')
        return reverse('task-delete', kwargs={'slug':obj.slug}, request=request)