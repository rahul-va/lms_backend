from rest_framework import serializers

from module_management.models import Module

class ModuleSerailizer(serializers.ModelSerializer):

    class Meta:

        model = Module

        fields = "__all__"

        read_only_fields = ["id","course","order","slug","created_at","updated_at"]