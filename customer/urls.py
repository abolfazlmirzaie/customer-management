from rest_framework_nested import routers

from customer.views import CustomerViewSet, NoteViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')


customers_router = routers.NestedDefaultRouter(router, r'customers', lookup='customer')
customers_router.register(r'notes', NoteViewSet, basename='customer-notes')





urlpatterns = router.urls + customers_router.urls

