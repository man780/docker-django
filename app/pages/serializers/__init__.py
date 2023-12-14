from datetime import datetime
from rest_framework.serializers import ModelSerializer


class BaseSerializer(ModelSerializer):

    def create(self, validated_data):
        # Automatically set created_time and created_user on create
        validated_data['created_time'] = datetime.now()
        validated_data['created_user'] = self.context['request'].user
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Automatically set updated_time and updated_user on update
        validated_data['updated_time'] = datetime.now()
        validated_data['updated_user'] = self.context['request'].user

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
