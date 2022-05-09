from rest_framework.routers import DefaultRouter
from dnd import views

router = DefaultRouter()
router.register(r'elements', views.ElementViewSet, basename='elements')
router.register(r'conditions', views.ConditionViewSet, basename='conditions')
router.register(r'effects', views.EffectViewSet, basename='effects')
router.register(r'dnd_classes', views.Dnd_ClassViewSet, basename='dnd_classes')
router.register(r'spell_components', views.Spell_ComponentViewSet, basename='spell_components')
router.register(r'spells', views.SpellViewSet, basename='spells')
urlpatterns = router.urls