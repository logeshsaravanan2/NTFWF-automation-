import copy
from base_test_runner import BaseTestRunnerUI
import tkinter as tk

# Define your testcases and testcase_descriptions as before
testcase_descriptions = [
"1. Standard case: Valid payload with all required fields present.",
"2. Missing optional field: Payload missing an optional field to test default handling.",
"3. Invalid tracking number: Payload with an invalid UPS tracking number format.",
"4. Future delivery date: Payload with a delivery date set in the future to test date validation.",
"5. Empty payload: Payload with no dataAttributes to test handling of empty inputs."
]

base_payload = {
    "requestId": "10106357368888669_1",
    "sendTimeStamp": "2025-03-21T17:07:21.866-05:00",
    "messageSrcSystem": "FFWF",
    "notificationReason": "FFWF.UpsShipmentEvent",
    "dataAttributes": [
        {
            "name": "NOTIFICATION_STACK",
            "value": "Ordering"
        },
        {
            "name": "ASSOC_PROD_ID",
            "value": "3527537054"
        },
        {
            "name": "MARKET",
            "value": "I"
        },
        {
            "name": "TEMPLATE",
            "value": "ECOM.ORDERING.SHIPPINGCONF"
        },
        {
            "name": "LANGUAGE",
            "value": "English"
        },
        {
            "name": "COMPANY",
            "value": "LCTL"
        },
        {
            "name": "BAN",
            "value": "497822050"
        },
        {
            "name": "ORDER_SOURCE",
            "value": "BM"
        },
        {
            "name": "ORDER_CREATE_DATE",
            "value": "03-21-2025"
        },
        {
            "name": "SHIP_ADDRESS_LINE1",
            "value": "2816 BURGOS DR"
        },
        {
            "name": "SHIP_ADDRESS_LINE2",
            "value": ""
        },
        {
            "name": "SHIP_ADDRESS_CITY",
            "value": "THE VILLAGES"
        },
        {
            "name": "SHIP_ADDRESS_STATE",
            "value": "FL"
        },
        {
            "name": "SHIP_ADDRESS_ZIP",
            "value": "32162"
        },
        {
            "name": "SHIPPING_NAME",
            "value": "STEVEN KIELEY"
        },
        {
            "name": "UPS_TRACKING_NUMBER",
            "value": "1ZX738X71365538449"
        },
        {
            "name": "DELIVERY_DATE",
            "value": "03-24-2025"
        },
        {
            "name": "ACTUAL_SHIP_DATE",
            "value": "03-21-2025"
        },
        {
            "name": "COMPANY_OWNER_ID",
            "value": "1"
        }
    ]
}

testcases = []
# Generate multiple test cases by modifying the base payload
# 1. Standard case
tc1 = copy.deepcopy(base_payload)
testcases.append(tc1)

# 2. Missing optional field (e.g., SHIP_ADDRESS_LINE2)
tc2 = copy.deepcopy(base_payload)
tc2["dataAttributes"] = [attr for attr in tc2["dataAttributes"] if attr["name"] != "SHIP_ADDRESS_LINE2"]
testcases.append(tc2)

# 3. Invalid tracking number
tc3 = copy.deepcopy(base_payload)
for attr in tc3["dataAttributes"]:
    if attr["name"] == "UPS_TRACKING_NUMBER":
        attr["value"] = "INVALID_TRACKING_123"
testcases.append(tc3)

# 4. Future delivery date
tc4 = copy.deepcopy(base_payload)
for attr in tc4["dataAttributes"]:
    if attr["name"] == "DELIVERY_DATE":
        attr["value"] = "12-31-2099"
testcases.append(tc4)

# 5. Empty payload
tc5 = copy.deepcopy(base_payload)
tc5["dataAttributes"] = []
testcases.append(tc5)

# api_urls = [
#     "https://ntfwf-ordering-service-test1.rke-odc-test.corp.intranet/api/notification/order/config"
# ]


