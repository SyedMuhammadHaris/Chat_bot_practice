import logging
import requests

hasattr
from utils.common import get_formatted_date


def get_formatted_shipment_date(order_id):
    try:
        order_api_url = "https://orderstatusapi-dot-organization-project-311520.uc.r.appspot.com/api/getOrderStatus"
        response = requests.post(order_api_url, {"orderId": order_id})
        json_res = response.json()
        
        if "shipmentDate" in json_res and json_res["shipmentDate"]:
            shipment_date = json_res["shipmentDate"]
            formatted_shipment_date = get_formatted_date(shipment_date)
            return f"Your order {order_id} will be shipped on {formatted_shipment_date}"
        else:
            error_message = json_res["error"]
            return f"{error_message}"

    except Exception as e:
        logging.exception(e)
        return "Something went wrong!"
