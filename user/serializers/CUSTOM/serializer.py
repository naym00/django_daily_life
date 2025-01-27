from rest_framework import serializers
from help.common.a import A as HELP
from user import models as M_USER

class Coverphotosrlzr(serializers.ModelSerializer):
    class Meta:
        model =M_USER.Coverphoto
        fields=['id', 'user', 'image', 'is_active']

class Profilepicsrlzr(serializers.ModelSerializer):
    class Meta:
        model=M_USER.Profilepic
        fields=['id', 'user', 'image', 'is_active']

class Usersrlzr(serializers.ModelSerializer):
    profilepic=serializers.SerializerMethodField()
    profilepic_user=Profilepicsrlzr(many=True)
    coverphoto=serializers.SerializerMethodField()
    coverphoto_user=Coverphotosrlzr(many=True)
    
    def get_profilepic(self, instance):
        profilepic=HELP().getProfilePic(instance)
        serializer = Profilepicsrlzr(instance=profilepic, many=False)
        return serializer.data
    
    def get_coverphoto(self, instance):
        coverphoto=HELP().getCoverPhoto(instance)
        serializer = Coverphotosrlzr(instance=coverphoto, many=False)
        return serializer.data
    
    class Meta:
        model=M_USER.User
        fields=['id', 'phone', 'gender', 'profilepic', 'profilepic_user', 'coverphoto', 'coverphoto_user']