from rest_framework import serializers
# import user model
from .models import User


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        
        #specify the model witch want to ssert
        model = User
        #specif the fields of table
        fields = "__all__"
        db_table = 'user'
        
 