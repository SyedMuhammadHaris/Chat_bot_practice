from django.urls import path

from apps.webhook_service.views.webhook_view import WebhookApiView


urlpatterns = [
    path("dialogflow", WebhookApiView.as_view(), name="dialogflow"),
]