from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from .models import (
    Character,
    Skill,
    Weapon,
    Item,
    Ability,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'id', 'username')


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='character-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Character
        fields = ('id', 'url', 'first_name', 'last_name', 'surname', 'player', 'dndclass', 'dndarchetype', 'level', 'str', 'dex',
                  'con', 'int', 'wis', 'cha', 'save_str', 'save_dex', 'save_con', 'save_int', 'save_wis', 'save_cha', 'ac', 'initiative', )
        # extra_kwargs = extra_initial(model)


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='skill-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Skill
        fields = ('id', 'url',
                  'name',
                  'stat',
                  'mastery',
                  'expertise',
                  'bonus',
                  'character',)
        # extra_kwargs = extra_initial(model)


class WeaponSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='contact-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Weapon
        fields = ('id', 'url',
                  'name', 'surname', 'description', 'stat', 'mastery', 'bonus', 'dmg', 'character',)
        # extra_kwargs = extra_initial(model)


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='contact-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Item
        fields = ('id', 'url', 'name', 'description',
                  'weight', 'stack', 'character',)
        # extra_kwargs = extra_initial(model)


class AbilitySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='contact-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Ability
        fields = ('id', 'url', 'name', 'description', 'character')
        # extra_kwargs = extra_initial(model)
