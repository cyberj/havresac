
from django.contrib.auth.models import User, Group
from django.db.models import Max, Sum
# from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from character import serializers

from .models import (
    Character,
    Skill,
    Weapon,
    Item,
    Ability,
)


class UserViewSet(viewsets.ModelViewSet):

    """
    Api endpoint that allow Users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class CharacterViewSet(viewsets.ModelViewSet):

    """
    Api endpoint that allow Characters to be viewed or edited
    """
    queryset = Character.objects.all()
    serializer_class = serializers.CharacterSerializer

    # def get_queryset(self):
    #     """
    #     This view should return a list of all contacts
    #     for the currently authenticated user.
    #     """
    #     user = self.request.user
    #     # We can't use self.queryset cause o transactionals tests cases
    #     query = Character.objects.all()
    #     # if not user.is_staff:
    #     #     query = query.filter(character__grouppermission__group__user=user,
    #     #                          character__grouppermission__can_read=True)
    #     return query

    @detail_route(methods=['get'])
    def full(self, request, pk=None):
        """Full PJ sheet
        """
        character = self.get_object()
        # print(character)
        result = {}
        result["character"] = serializers.CharacterSerializer(
            character, context={'request': request}).data

        skills = Skill.objects.filter(character=character)
        result["skills"] = [serializers.SkillSerializer(
            skill, context={'request': request}).data for skill in skills]

        weapons = Weapon.objects.filter(character=character)
        result["weapons"] = [serializers.WeaponSerializer(
            weapon, context={'request': request}).data for weapon in weapons]

        items = Item.objects.filter(character=character)
        result["items"] = [serializers.ItemSerializer(
            item, context={'request': request}).data for item in items]

        abilities = Ability.objects.filter(character=character)
        result["abilitys"] = [serializers.AbilitySerializer(
            ability, context={'request': request}).data for ability in abilities]

        return Response(result)


class SkillViewSet(viewsets.ModelViewSet):

    """
    Api endpoint that allow Skills to be viewed or edited
    """
    queryset = Skill.objects.all()
    serializer_class = serializers.SkillSerializer


class WeaponViewSet(viewsets.ModelViewSet):

    """
    Api endpoint that allow Weapons to be viewed or edited
    """
    queryset = Weapon.objects.all()
    serializer_class = serializers.WeaponSerializer


class ItemViewSet(viewsets.ModelViewSet):

    """
    Api endpoint that allow Items to be viewed or edited
    """
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer


class AbilityViewSet(viewsets.ModelViewSet):

    """
    Api endpoint that allow Abilitys to be viewed or edited
    """
    queryset = Ability.objects.all()
    serializer_class = serializers.AbilitySerializer
