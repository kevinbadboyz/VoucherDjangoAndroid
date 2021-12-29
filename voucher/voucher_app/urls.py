from django.urls import path
from voucher_app import views
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'voucher_app'

urlpatterns = [    
    path('api/game/', views.GameList.as_view()),
    path('api/game/<int:pk>/', views.GameDetail.as_view()),
    path('api/game/search/', views.GameListAPIView.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)

