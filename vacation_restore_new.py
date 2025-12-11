import copy
from base_test_runner import BaseTestRunnerUI
import tkinter as tk

# Define your testcases and testcase_descriptions as before
# List of test cases with descriptive names
testcase_descriptions = [
    "1: success",
    "2: request id is mandatory",
    "request id starts with BMOM",
    "3: messageSrcSystem should be BMOM",
    "4: ban should be 9 digits",
    "5: notification id should be ECOM.Ordering.VacationRestore",
    "6: one of the email or sms should be present - case 1: both missing",
    "7: one of the email or sms should be present - case 2: only email missing",
    "8: one of the email or sms should be present - case 3: only sms missing",
    "9: product tn should be 10 digits",
    "10: product details should be POTS or HSI or HSI,POTS - case 1: null",
    "11: product details should be POTS or HSI or HSI,POTS - case 2: HSI only",
    "12: product details should be POTS or HSI or HSI,POTS - case 3: POTS",
    "13: product details should be POTS or HSI or HSI,POTS - case 4: POTS,HSI",
    "14: company should be LQ or CTL - case 1: LCTL",
    "15: company should be LQ or CTL - case 2: LQ",
    "16: company should be LQ or CTL - case 3: invalid value",
    "17: service address line1 should not be empty",
    "18: service address city should not be empty",
    "19: service address state should not be empty",
    "20: service address zip should not be empty",
    "21: order number should not be empty",
    "22: order type should not be empty",
    "23: market should be I - case 1: valid",
    "24: market should be I - case 2: invalid",
    "25: order create date should be in YYYYMMDD format - case 1: valid",
    "26: order create date should be in YYYYMMDD format - case 2: invalid",
    "27: order create date should be in YYYYMMDD format - case 3: empty",
    "28: order due date should be in MM-DD-YYYY format - case 1: valid",
    "29: order due date should be in MM-DD-YYYY format - case 2: invalid",
    "30: order due date should be in MM-DD-YYYY format - case 3: empty",
    "31: using smb account",
    "32: using prepaid individual account",
    "33: using prepaid business account"

]

base_payload = {
    "requestId": "BMOM_1754522109917",
    "sendTimeStamp": "2025-08-06T23:15:09.917",
    "messageSrcSystem": "BMOM",
    "notificationReason": "BMOM.OrderConfirmation",
    "dataAttributes": [
        {
            "name": "NOTIFICATION_ID",
            "value": "Ecom.Ordering.VacationRestore"
        },
        {
            "name": "TEMPLATE",
            "value": "Ecom.Ordering.VacationRestore"
        },
        {
            "name": "BAN",
            "value": "300518801"
        },
        {
            "name": "FIRST_NAME",
            "value": "DANIEL"
        },
        {
            "name": "LAST_NAME",
            "value": "CALOHAN"
        },
        {
            "name": "CUST_EMAIL_ADDRESS",
            "value": "Saravanan.s@lumen.com"
        },
        {
            "name": "SMS_NUMBER",
            "value": "3602980921"
        },
        {
            "name": "PRODUCT_TN",
            "value": "3603784840"
        },
        {
            "name": "PRODUCT_DETAIL",
            "value": "POTS"
        },
        {
            "name": "COMPANY",
            "value": "LCTL"
        },
        {
            "name": "SERVICE_ADDRESS_LINE1",
            "value": "22 TWO BARN FARM LN WA 98250"
        },
        {
            "name": "SERVICE_ADDRESS_CITY",
            "value": "SAN JUAN IS"
        },
        {
            "name": "SERVICE_ADDRESS_STATE",
            "value": "WA"
        },
        {
            "name": "SERVICE_ADDRESS_ZIP",
            "value": "98250"
        },
        {
            "name": "LANGUAGE",
            "value": "ENGLISH"
        },
        {
            "name": "ORDER_NUMBER",
            "value": "1023157808"
        },
        {
            "name": "USO_ORDER_NUMBER",
            "value": ""
        },
        {
            "name": "ORDER_TYPE",
            "value": "VACATIONRESTORE"
        },
        {
            "name": "MARKET",
            "value": "I"
        },
        {
            "name": "ORDER_CREATE_DATE",
            "value": "20250225"
        },
        {
            "name": "ORDER_DUE_DATE",
            "value": "02-27-2025"
        },
        {
            "name": "PRODUCT_ID",
            "value": "3603784840"
        }

    ]
}


testcases = []

#1: success
tc1 = copy.deepcopy(base_payload)
testcases.append(tc1)

#2: request id is mandatory
tc2 = copy.deepcopy(base_payload)
tc2["requestId"] = ""
testcases.append(tc2)

# request id starts with BMOM
tcr = copy.deepcopy(base_payload)
tcr["requestId"] = "TEST_1754522109917"
testcases.append(tcr)

# 3. messageSrcSystem should be BMOM
tc3 = copy.deepcopy(base_payload)
tc3["messageSrcSystem"] = "TESTSYS"
testcases.append(tc3)

# 4. ban should be 9 digits
tc4 = copy.deepcopy(base_payload)
for attr in tc4["dataAttributes"]:
    if attr["name"] == "BAN":
        attr["value"] = "12345"
testcases.append(tc4)

# 5. notification id should be ECOM.Ordering.VacationRestore
tc5 = copy.deepcopy(base_payload)
for attr in tc5["dataAttributes"]:
    if attr["name"] == "NOTIFICATION_ID":
        attr["value"] = "VacationRestore"
testcases.append(tc5)

# 6. one of the email or sms should be present - case 1: both missing
tc6 = copy.deepcopy(base_payload)
for attr in tc6["dataAttributes"]:
    if attr["name"] == "CUST_EMAIL_ADDRESS":
        attr["value"] = ""
    if attr["name"] == "SMS_NUMBER":
        attr["value"] = ""
testcases.append(tc6)

# 7. one of the email or sms should be present - case 2: only email missing
tc7 = copy.deepcopy(base_payload)
for attr in tc7["dataAttributes"]:
    if attr["name"] == "CUST_EMAIL_ADDRESS":
        attr["value"] = ""
testcases.append(tc7)

# 8. one of the email or sms should be present - case 3: only sms missing
tc8 = copy.deepcopy(base_payload)
for attr in tc8["dataAttributes"]:
    if attr["name"] == "SMS_NUMBER":
        attr["value"] = ""
testcases.append(tc8)

# 9. product tn should be 10 digits
tc9 = copy.deepcopy(base_payload)
for attr in tc9["dataAttributes"]:
    if attr["name"] == "PRODUCT_TN":
        attr["value"] = "123456"
testcases.append(tc9)

# 10. product details should be POTS or HSI or HSI,POTS - case 1: null
tc10 = copy.deepcopy(base_payload)
for attr in tc10["dataAttributes"]:
    if attr["name"] == "PRODUCT_DETAIL":
        attr["value"] = ""
testcases.append(tc10)

# 11. product details should be POTS or HSI or HSI,POTS - case 2: HSI only
tc11 = copy.deepcopy(base_payload)
for attr in tc11["dataAttributes"]:
    if attr["name"] == "PRODUCT_DETAIL":
        attr["value"] = "HSI"
testcases.append(tc11)

# 12. product details should be POTS or HSI or HSI,POTS - case 3: POTS
tc12 = copy.deepcopy(base_payload)
for attr in tc12["dataAttributes"]:
    if attr["name"] == "PRODUCT_DETAIL":
        attr["value"] = "POTS"
testcases.append(tc12)

# 13. product details should be POTS or HSI or HSI,POTS - case 4: POTS,HSI
tc13 = copy.deepcopy(base_payload)
for attr in tc13["dataAttributes"]:
    if attr["name"] == "PRODUCT_DETAIL":
        attr["value"] = "POTS,HSI"
testcases.append(tc13)

# 14. company should be LQ or CTL - case 1: CTL
tc14 = copy.deepcopy(base_payload)
for attr in tc14["dataAttributes"]:
    if attr["name"] == "COMPANY":
        attr["value"] = "LCTL"
testcases.append(tc14)

# 15. company should be LQ or CTL - case 2: LQ
tc15 = copy.deepcopy(base_payload)
for attr in tc15["dataAttributes"]:
    if attr["name"] == "COMPANY":
        attr["value"] = "LQ"
testcases.append(tc15)

# 16. company should be LQ or CTL - case 3: invalid value
tc16 = copy.deepcopy(base_payload)
for attr in tc16["dataAttributes"]:
    if attr["name"] == "COMPANY":
        attr["value"] = "XYZ"
testcases.append(tc16)

# 17. service address line1 should not be empty
tc17 = copy.deepcopy(base_payload)
for attr in tc17["dataAttributes"]:
    if attr["name"] == "SERVICE_ADDRESS_LINE1":
        attr["value"] = ""
testcases.append(tc17)

# 18. service address city should not be empty
tc18 = copy.deepcopy(base_payload)
for attr in tc18["dataAttributes"]:
    if attr["name"] == "SERVICE_ADDRESS_CITY":
        attr["value"] = ""
testcases.append(tc18)

# 19. service address state should not be empty
tc19 = copy.deepcopy(base_payload)
for attr in tc19["dataAttributes"]:
    if attr["name"] == "SERVICE_ADDRESS_STATE":
        attr["value"] = ""
testcases.append(tc19)

# 20. service address zip should not be empty
tc20 = copy.deepcopy(base_payload)
for attr in tc20["dataAttributes"]:
    if attr["name"] == "SERVICE_ADDRESS_ZIP":
        attr["value"] = ""
testcases.append(tc20)

# 21. order number should not be empty
tc21 = copy.deepcopy(base_payload)
for attr in tc21["dataAttributes"]:
    if attr["name"] == "ORDER_NUMBER":
        attr["value"] = ""
testcases.append(tc21)

# 22. order type should not be empty
tc22 = copy.deepcopy(base_payload)
for attr in tc22["dataAttributes"]:
    if attr["name"] == "ORDER_TYPE":
        attr["value"] = ""
testcases.append(tc22)

# 23. market should be I - case 1: valid
tc23 = copy.deepcopy(base_payload)
for attr in tc23["dataAttributes"]:
    if attr["name"] == "MARKET":
        attr["value"] = "I"
testcases.append(tc23)

# 24. market should be I - case 2: invalid
tc24 = copy.deepcopy(base_payload)
for attr in tc24["dataAttributes"]:
    if attr["name"] == "MARKET":
        attr["value"] = "X"
testcases.append(tc24)

# 25. order create date should be in YYYYMMDD format - case 1: valid
tc25 = copy.deepcopy(base_payload)
for attr in tc25["dataAttributes"]:
    if attr["name"] == "ORDER_CREATE_DATE":
        attr["value"] = "20250220"
testcases.append(tc25)

# 26. order create date should be in YYYYMMDD format - case 2: invalid
tc26 = copy.deepcopy(base_payload)
for attr in tc26["dataAttributes"]:
    if attr["name"] == "ORDER_CREATE_DATE":
        attr["value"] = "20-02-2025"
testcases.append(tc26)

# 27. order create date should be in YYYYMMDD format - case 3: empty
tc27 = copy.deepcopy(base_payload)
for attr in tc27["dataAttributes"]:
    if attr["name"] == "ORDER_CREATE_DATE":
        attr["value"] = ""
testcases.append(tc27)

# 28. order due date should be in MM-DD-YYYY format - case 1: valid
tc28 = copy.deepcopy(base_payload)
for attr in tc28["dataAttributes"]:
    if attr["name"] == "ORDER_DUE_DATE":
        attr["value"] = "07-21-2025"
testcases.append(tc28)

# 29. order due date should be in MM-DD-YYYY format - case 2: invalid
tc29 = copy.deepcopy(base_payload)
for attr in tc29["dataAttributes"]:
    if attr["name"] == "ORDER_DUE_DATE":
        attr["value"] = "2025/07/21"
testcases.append(tc29)

# 30. order due date should be in MM-DD-YYYY format - case 3: empty
tc30 = copy.deepcopy(base_payload)
for attr in tc30["dataAttributes"]:
    if attr["name"] == "ORDER_DUE_DATE":
        attr["value"] = ""
testcases.append(tc30)

# 31. using smb account
tc31 = copy.deepcopy(base_payload)
for attr in tc4["dataAttributes"]:
    if attr["name"] == "BAN":
        attr["value"] = "497822050"
testcases.append(tc31)

#32. using prepaid individual account
tc32 = copy.deepcopy(base_payload)
for attr in tc4["dataAttributes"]:
    if attr["name"] == "BAN":
        attr["value"] = "PPB06029221"
testcases.append(tc32)

# 33. using prepaid business account
tc33 = copy.deepcopy(base_payload)
for attr in tc4["dataAttributes"]:
    if attr["name"] == "BAN":
        attr["value"] = "PPB06033465"
testcases.append(tc33)



# api_urls = [
#     "https://ntfwf-ordering-service-test1.rke-odc-test.corp.intranet/api/notification/order/config"
# ]
class ShipConfTestRunnerUI(BaseTestRunnerUI):
    def __init__(self, master):
        super().__init__(master, testcases, testcase_descriptions, "ECOM.ORDERING.VACATIONRESTORE")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShipConfTestRunnerUI(root)
    root.mainloop()
