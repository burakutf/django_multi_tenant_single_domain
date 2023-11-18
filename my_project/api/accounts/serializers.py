from rest_framework import serializers


from my_project.apps.accounts.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        organization = request.user.organization

        if organization:
            validated_data['organization'] = organization
            return super().create(validated_data)
