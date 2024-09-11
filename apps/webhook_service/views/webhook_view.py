import json
import logging
from django.http import JsonResponse
from rest_framework.views import APIView
from utils.custom_response import ErrorResponse, SuccessResponse
from utils.get_shipment_date import get_formatted_shipment_date
from rest_framework import status
from rest_framework.response import Response

class WebhookApiView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            print(data)
            query_text = data.get("queryResult").get("queryText")
            parameters = data.get("queryResult").get("parameters")
            order_id = parameters.get("OrderId")
           
            shipment_date_response = get_formatted_shipment_date(order_id)
            print(shipment_date_response)
            return Response({"fulfillmentText": shipment_date_response})
            
        except Exception as e:
            logging.exception(e)
            status_code = e.status_code if hasattr(e, "status_code") else 422
            return ErrorResponse(message=str(e), status_code=status_code, data=None)


