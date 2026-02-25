import copy
from base_test_runner import BaseTestRunnerUI
import tkinter as tk

# Define your testcases and testcase_descriptions as before
testcase_descriptions = [
    "1. Valid payload",
    "2. Missing requestId",
    "3. Invalid messageSrcSystem",
    "4. Invalid TEMPLATE name",
    "5. Empty NOTIFICATION_STACK",
    "6. Missing BAN",
    "7. BAN length less than 9",
    "8. Missing UPS_TRACKING_NUMBER",
    "9. Missing ORDER_CREATE_DATE",
    "10. Missing DELIVERY_DATE",
    "11. Missing SHIPPING_NAME",
    "12. Missing ACTUAL_SHIP_DATE",
    "13. Missing all shipping address fields",
    "14. Missing one shipping address field (SHIP_ADDRESS_STATE)",
    "15. Invalid COMPANY value",
    "16. Invalid MARKET value"
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
# 1. success case
tc1 = copy.deepcopy(base_payload)
testcases.append(tc1)

#2. Request ID is mandatory
tc2 = copy.deepcopy(base_payload)
tc2["requestId"] = ""
testcases.append(tc2)

#3 MessageSourceSystem is mandatory
tc3 = copy.deepcopy(base_payload)
tc3["messageSrcSystem"] = "INVALID"
testcases.append(tc3)

#4. Template should be ECOM.ORDERING.SHIPPINGCONF
tc4 = copy.deepcopy(base_payload)
tc4["dataAttributes"][3]["value"] = "INVALID.TEMPLATE.NAME"
testcases.append(tc4)

#5. Notification Stack should be mandatory
tc5 = copy.deepcopy(base_payload)
tc5["dataAttributes"][0]["value"] = ""
testcases.append(tc5)

#6. BAN or BAID should be present - both missing
tc6 = copy.deepcopy(base_payload)
for attr in tc6["dataAttributes"]:
    if attr["name"] == "BAN":
        attr["value"] = ""
        break
testcases.append(tc6)

#7. BAN length should not be less than 9
tc7 = copy.deepcopy(base_payload)
for attr in tc7["dataAttributes"]:
    if attr["name"] == "BAN":
        attr["value"] = "12345"
        break
testcases.append(tc7)

#8.UPSTrackingNumber is mandatory
tc8 = copy.deepcopy(base_payload)
for attr in tc8["dataAttributes"]:
    if attr["name"] == "UPS_TRACKING_NUMBER":
        attr["value"] = ""
        break
testcases.append(tc8)

#9.OrderDate is mandatory
tc9 = copy.deepcopy(base_payload)
for attr in tc9["dataAttributes"]:
    if attr["name"] == "ORDER_CREATE_DATE":
        attr["value"] = ""
        break
testcases.append(tc9)

#10.DeliveryDate is mandatory
tc10 = copy.deepcopy(base_payload)
for attr in tc10["dataAttributes"]:
    if attr["name"] == "DELIVERY_DATE":
        attr["value"] = ""
        break
testcases.append(tc10)

#11. ShippingName is mandatory
tc11 = copy.deepcopy(base_payload)
for attr in tc11["dataAttributes"]:
    if attr["name"] == "SHIPPING_NAME":
        attr["value"] = ""
        break
testcases.append(tc11)

#12. ActualShipDate is mandatory
tc12 = copy.deepcopy(base_payload)
for attr in tc12["dataAttributes"]:
    if attr["name"] == "ACTUAL_SHIP_DATE":
        attr["value"] = ""
        break
testcases.append(tc12)

#13 Shipping Address1 or ShipCity or ShipState or ShipZip – one of the should be present - all missing
tc13 = copy.deepcopy(base_payload)
for attr in tc13["dataAttributes"]:
    if attr["name"] == "SHIP_ADDRESS_LINE1":
        attr["value"] = ""
    if attr["name"] == "SHIP_ADDRESS_CITY":
        attr["value"] = ""
    if attr["name"] == "SHIP_ADDRESS_STATE":
        attr["value"] = ""
    if attr["name"] == "SHIP_ADDRESS_ZIP":
        attr["value"] = ""
testcases.append(tc13)

#14. Shipping Address1 or ShipCity or ShipState or ShipZip – one of the should be present - one missing (ShipState)
tc14 = copy.deepcopy(base_payload)
for attr in tc14["dataAttributes"]:
    if attr["name"] == "SHIP_ADDRESS_STATE":
        attr["value"] = ""
        break
testcases.append(tc14)

#15. Company should be equal to “LCTL”
tc15 = copy.deepcopy(base_payload)
for attr in tc15["dataAttributes"]:
    if attr["name"] == "COMPANY":
        attr["value"] = "INVALID_COMPANY"
        break
testcases.append(tc15)

#16. MarketType should be either “I” or “S”
tc16 = copy.deepcopy(base_payload)
for attr in tc16["dataAttributes"]:
    if attr["name"] == "MARKET":
        attr["value"] = "X"
        break
testcases.append(tc16)



# api_urls = [
#     "https://ntfwf-ordering-service-test1.rke-odc-test.corp.intranet/api/notification/order/config"
# ]


