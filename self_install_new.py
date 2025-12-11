import copy

from base_test_runner import BaseTestRunnerUI
import tkinter as tk

# Define your testcases and testcase_descriptions as before
# List of test cases with descriptive names
testcase_descriptions = [
    "1. Valid payload",
    "2. Missing requestId",
    "3. Invalid requestId prefix",
    "4. Invalid messageSrcSystem",
    "5. Empty DispatchReason",
    "6. Invalid DispatchReason",
    "7. Empty ORDER_DUE_DATE",
    "8. Empty notificationReason",
    "9. Empty NOTIFICATION_STACK",
    "10. Empty COMPANY",
    "11. Empty CUSTOMER_TYPE",
    "12. Invalid CUSTOMER_TYPE",
    "13. Empty ORDER_NUMBER"

]

base_payload = {
    "requestId": "CLICK_1744898400386",
    "sendTimeStamp": "2025-04-17T14:00:00.386Z",
    "messageSrcSystem": "CLICK",
    "notificationReason": "CLICK.SelfInstall",
    "dataAttributes": [
        {
            "name": "FIRST_NAME",
            "value": "DARLA HITE"
        },
        {
            "name": "ORDER_NUMBER",
            "value": "1022601412"
        },
        {
            "name": "DISPATCH_REASON",
            "value": "DueDateMinusOne"
        },
        {
            "name": "BAN",
            "value": "PPB04784162"
        },
        {
            "name": "PRODUCT_TN",
            "value": "8708951746"
        },
        {
            "name": "ORDER_DUE_DATE",
            "value": "04-18-2025"
        },
        {
            "name": "TEMPLATE",
            "value": "ECOM.ACCTMGMT.TECH"
        },
        {
            "name": "NOTIFICATION_STACK",
            "value": "Ordering"
        },
        {
            "name": "COMPANY",
            "value": "LCTL"
        },
        {
            "name": "CUSTOMER_TYPE",
            "value": "CONSUMER"
        }
    ]
}



testcases = []
# 1. Valid payload
tc1 = copy.deepcopy(base_payload)
testcases.append(tc1)

# 2.RequestId is mandatory and should be started with “CLICK”, case1: Missing requestId
tc2 = copy.deepcopy(base_payload)
tc2["requestId"] = ""
testcases.append(tc2)

# 3. RequestId is mandatory and should be started with “CLICK”, case2: starts with invalid prefix
tc3 = copy.deepcopy(base_payload)
tc3["requestId"] = "INVALID_1744898400386"
testcases.append(tc3)

# MessageSourceSystem must be “CLICK”.
tc4 = copy.deepcopy(base_payload)
tc4["messageSrcSystem"] = "INVALID_SYSTEM"
testcases.append(tc4)

# 5. DispatchReason should not be empty , It should be either “DueDateMinusOne” or “DispatchComplete”. case1: empty DispatchReason
tc5 = copy.deepcopy(base_payload)
for attr in tc5["dataAttributes"]:
    if attr["name"] == "DISPATCH_REASON":
        attr["value"] = ""
        break
testcases.append(tc5)
# 6. DispatchReason should not be empty , It should be either “DueDateMinusOne” or “DispatchComplete”. case2: invalid DispatchReason
tc6 = copy.deepcopy(base_payload)
for attr in tc6["dataAttributes"]:
    if attr["name"] == "DISPATCH_REASON":
        attr["value"] = "INVALID_REASON"
        break
testcases.append(tc6)

# 7. DueDate should not be empty.
tc7 = copy.deepcopy(base_payload)
for attr in tc7["dataAttributes"]:
    if attr["name"] == "ORDER_DUE_DATE":
        attr["value"] = ""
        break
testcases.append(tc7)

# 8. “NotificationId” should not be empty.
tc8 = copy.deepcopy(base_payload)
tc8["notificationReason"] = ""
testcases.append(tc8)

# 9. “NotificationStack” should not be empty.
tc9 = copy.deepcopy(base_payload)
for attr in tc9["dataAttributes"]:
    if attr["name"] == "NOTIFICATION_STACK":
        attr["value"] = ""
        break
testcases.append(tc9)

# 10.“Company” should not be empty.
tc10 = copy.deepcopy(base_payload)
for attr in tc10["dataAttributes"]:
    if attr["name"] == "COMPANY":
        attr["value"] = ""
        break
testcases.append(tc10)

# 11. “CustomerType” should not be empty , It should be either “CONSUMER” or “SMB”. case1: empty CustomerType
tc11 = copy.deepcopy(base_payload)
for attr in tc11["dataAttributes"]:
    if attr["name"] == "CUSTOMER_TYPE":
        attr["value"] = ""
        break
testcases.append(tc11)
# 12. “CustomerType” should not be empty , It should be either “CONSUMER” or “SMB”. case2: invalid CustomerType
tc12 = copy.deepcopy(base_payload)
for attr in tc12["dataAttributes"]:
    if attr["name"] == "CUSTOMER_TYPE":
        attr["value"] = "INVALID_TYPE"
        break
testcases.append(tc12)

# 13. OrderNumber should not be empty.
tc13 = copy.deepcopy(base_payload)
for attr in tc13["dataAttributes"]:
    if attr["name"] == "ORDER_NUMBER":
        attr["value"] = ""
        break
testcases.append(tc13)

# api_urls = [
#     "https://ntfwf-ordering-service-test1.rke-odc-test.corp.intranet/api/notification/order/config"
# ]
