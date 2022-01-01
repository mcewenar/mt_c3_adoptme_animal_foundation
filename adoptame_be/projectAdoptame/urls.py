from django.contrib import admin
from django.urls import path, include
from appAdoptame import views
from appAdoptame.views.AdoptanteView import AdoptanteListCreateView,AdoptanteRetrieveUpdateDestroy
from appAdoptame.views.donanteview import DonanteListCreateView,DonanteRetrieveUpdateDestroy,DonanteListAverage
from appAdoptame.views.userAdminView import UserAdminListCreateView,UserAdminRetrieveUpdateDestroy
from appAdoptame.views.mascotaView import MascotaListCreateView, MascotaRetrieveUpdateDestroyAPIView
from appAdoptame.views.solicitudView import SolicitudesListCreateView, SolicitudRetrieveUpdateDestroy


from django.contrib.sites.models import Site
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adoptantes/', views.AdoptanteListCreateView.as_view()),
    path('adoptante/<int:pk>', views.AdoptanteRetrieveUpdateDestroy.as_view()),
    path('useradmins/', views.UserAdminListCreateView.as_view()),
    path('useradmin/<int:pk>', views.UserAdminRetrieveUpdateDestroy.as_view()),
    path('donantes/', views.DonanteListCreateView.as_view()),
    path('donante/<int:pk>', views.DonanteRetrieveUpdateDestroy.as_view()),
    path('mascotas/', views.MascotaListCreateView.as_view()),
    path('mascota/<int:pk>', views.MascotaRetrieveUpdateDestroyAPIView.as_view()),
    path('donantesavg/',views.DonanteListAverage.as_view()),    
    path('solicitudes/',views.SolicitudesListCreateView.as_view()),
    path('solicitud/<int:pk>',views.SolicitudRetrieveUpdateDestroy.as_view()),

    path('useradmin/rest-auth/', include('rest_auth.urls')),
    path('useradmin/rest-auth/registration/', include('rest_auth.registration.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.unregister(Site)