from django.conf.urls import include, url
# from django.views.generic.base import TemplateView
# # , RedirectView
# # from django.views.decorators.csrf import ensure_csrf_cookie
#
# # from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from character import api


router = routers.DefaultRouter()
router.register(r'character', api.CharacterViewSet)
router.register(r'skill', api.SkillViewSet)
router.register(r'weapon', api.WeaponViewSet)
router.register(r'item', api.ItemViewSet)
router.register(r'ability', api.AbilityViewSet)
# router.register(r'user', api.UserViewSet)


urlpatterns = [

]

urlpatterns += router.urls
