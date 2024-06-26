
from django.urls import path,include
from rest_framework import routers
from api.views import Companyviewset,Empolyviewset


from.import views
router=routers.DefaultRouter()
router.register(r'companies',Companyviewset)
router.register(r'employ',Empolyviewset)


urlpatterns = [
    path('',include(router.urls)),
    #path('home/',views.Companyviewset.as_view()),

]
