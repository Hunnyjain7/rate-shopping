from rest_framework.routers import DefaultRouter

from .views import ClientSubscriptionViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r"subscriptions", SubscriptionViewSet, basename="subscription")
router.register(
    r"client-subscriptions", ClientSubscriptionViewSet, basename="client-subscription"
)

urlpatterns = router.urls
