from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True  # Если уже авторизован - на главную
    ), name='login'),
    path('logout/', LogoutView.as_view(
        next_page='home'  # Явно указываем куда редиректить
    ), name='logout'),
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/create/', views.create_menu, name='menu_create'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.create_order, name='order_create'),
    path('autocomplete/client/', views.autocomplete_client, name='autocomplete_client'),
    path('orders/<int:pk>/edit/', views.edit_order, name='edit_order'),
    path('orders/<int:pk>/delete/', views.delete_order, name='delete_order'),
    path('reports/', views.reports, name='reports'),
    path('reports/popularity/', views.popularity_report, name='popularity_report'),
    path('reports/requirements/', views.requirements_report, name='requirements_report'),
    path('reports/profit/', views.profit_report, name='profit_report'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
