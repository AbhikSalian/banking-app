from django.urls import path,include
from django.shortcuts import redirect
from django.contrib import admin
# Include other imports
# from . import views

urlpatterns = [
    path('', lambda request: redirect('account_summary', account_id=1), name='home'),  # Redirect to account summary
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include your account urls
]
