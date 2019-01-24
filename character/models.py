from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group


# Create your models here.


class Character(models.Model):

    """
    RPG Character
    Character are a way to identify someone

    Todo:
     * Many things

    """

    first_name = models.CharField(_('Firstname'), max_length=100)
    last_name = models.CharField(_('Lastname'), max_length=100)
    surname = models.CharField(
        _('Surname'), blank=True, default="", max_length=100)
    player = models.CharField(_('Player'), blank=True,
                              default="", max_length=100)
    dndclass = models.CharField(_('DnDClass'), max_length=100)
    dndarchetype = models.CharField(
        _('DnDArchetype'), blank=True, default="", max_length=100)
    level = models.PositiveSmallIntegerField(_('Level'))
    str = models.PositiveSmallIntegerField(_('STR'), default=10)
    dex = models.PositiveSmallIntegerField(_('DEX'), default=10)
    con = models.PositiveSmallIntegerField(_('CON'), default=10)
    int = models.PositiveSmallIntegerField(_('INT'), default=10)
    wis = models.PositiveSmallIntegerField(_('WIS'), default=10)
    cha = models.PositiveSmallIntegerField(_('CHA'), default=10)

    save_str = models.BooleanField(_('Save STR'), default=False)
    save_dex = models.BooleanField(_('Save DEX'), default=False)
    save_con = models.BooleanField(_('Save CON'), default=False)
    save_int = models.BooleanField(_('Save INT'), default=False)
    save_wis = models.BooleanField(_('Save WIS'), default=False)
    save_cha = models.BooleanField(_('Save CHA'), default=False)

    ac = models.PositiveSmallIntegerField(_('ac'), default=10)
    initiative = models.PositiveSmallIntegerField(_('initiative'), default=10)
    # XXX - vard ?

    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ['last_name']


class Skill(models.Model):

    """
    RPG Character skill
    """

    name = models.CharField(_('name'), max_length=100)
    SKILL_CHOICES = (
        ('STR', _('STR')),
        ('DEX', _('DEX')),
        ('CON', _('CON')),
        ('INT', _('INT')),
        ('WIS', _('WIS')),
        ('CHA', _('CHA')),
    )
    stat = models.CharField(_('Stat'), max_length=4, default="STR",
                            choices=SKILL_CHOICES)

    mastery = models.BooleanField(_('Mastery'), default=False)
    expertise = models.BooleanField(_('Expertise'), default=False)
    bonus = models.PositiveSmallIntegerField(_('Bonus'), default=0)

    character = models.ForeignKey(
        'Character', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Weapon(models.Model):

    """
    RPG Character skill
    """

    name = models.CharField(_('name'), max_length=100)
    surname = models.CharField(_('surname'), max_length=100)
    description = models.TextField(_('Description'), max_length=100)

    SKILL_CHOICES = (
        ('STR', _('STR')),
        ('DEX', _('DEX')),
        ('CON', _('CON')),
        ('INT', _('INT')),
        ('WIS', _('WIS')),
        ('CHA', _('CHA')),
    )
    stat = models.CharField(_('Stat'), max_length=4, default="STR",
                            choices=SKILL_CHOICES)

    mastery = models.BooleanField(_('Mastery'), default=False)
    bonus = models.PositiveSmallIntegerField(_('Bonus'), default=0)

    dmg = models.CharField(_('Damage'), default="", max_length=64, blank=True)

    character = models.ForeignKey(
        'Character', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Item(models.Model):

    """
    RPG Character skill
    """

    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), max_length=100)
    weight = models.PositiveIntegerField(_('Bonus'), default=0)
    stack = models.PositiveIntegerField(_('Stack    '), default=0)

    character = models.ForeignKey(
        'Character', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Ability(models.Model):

    """
    RPG Character skill

    Packaging JS / composants VUEJS


    08h Présentation moi même / compétences de chacun / préférences
    09H Histoire JS / npm / install vuejs cli / start project [bower / webpack] / premières fonctions / 2 way binding / sass / less / type script
    10H require/ import (prévoir images) Bibliothèque de composants (Matérial vuetify component IO vueawesome) v-for v-if map/reduce/filter (photo sandwish)
        Canal de communication (event/props)
    11H ES6, Promesses, axios, async await
    12H

    14H Projet dnd5 découpage des taches en groupe BEM
    15H
    16H
    17H vuex
    18H

    """

    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'), max_length=100)

    character = models.ForeignKey(
        'Character', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
