import copy

from base_test_runner import BaseTestRunnerUI
import tkinter as tk

# Define your testcases and testcase_descriptions as before
# List of test cases with descriptive names
testcase_descriptions = [
   "1. Valid payload",
   "2. RequestId is mandatory",
   "3. MessageSrcSystem is mandatory",
   "4. NotificationReason is mandatory",
   "5. BillingSource should be CRIS or C2E or ENSEMBLE : case1: invalid BillingSource",
   "6. BillingSource should be CRIS or C2E or ENSEMBLE : case2: empty BillingSource",
   "7. BAN should not be empty",
   "8. EmailAddress & SMSAddress both should not  be empty: case1: empty EmailAddress",
   "9. EmailAddress & SMSAddress both should not  be empty: case2: both empty",
   "10. NotificationID should not be empty",
   "11. If BillingSource='C2E' , BAN should not empty",
   "12. Company should be either 'LQ' or 'LCTL' : case1: invalid Company",
   "13. Company should be either 'LQ' or 'LCTL' : case2: empty Company",
   "14. If Company is 'LCTL' , BAN should not be empty",
   "15. TemporaryVoicemailPIN should not empty",
   "16. VoicemailPlatform should be equal to 'LQ' or 'LCTL' : case1: invalid VoicemailPlatform",
   "17. VoicemailPlatform should be equal to 'LQ' or 'LCTL' : case2: empty VoicemailPlatform",
   "18. exttrackingnum should not be empty if Company='LQ'",
   "19. Exclude if Name is empty or length is less than 2",
   "20. scrnrid should not be empty"
]

base_payload = {

        "requestId": "891889900",
        "sendTimeStamp": "2025-10-24T18:13:00.450-05:00",
        "messageSrcSystem": "CTLRX",
        "notificationReason": "RX.VoicemailPINReset",
        "dataAttributes": [
            {
                "name": "COMPANY",
                "value": "LQ"
            },
            {
                "name": "TEMPLATE",
                "value": "ECOM.ACCTMGMT.VMRESET"
            },
            {
                "name": "CUSTOMER_CONTACT_NAME",
                "value": ""
            },
            {
                "name": "BAN",
                "value": "510992997"
            },
            {
                "name": "BILLING_SOURCE",
                "value": "ENSEMBLE"
            },
            {
                "name": "CUST_EMAIL_ADDRESS",
                "value": "saravanan.s@lumen.com"
            },
            {
                "name": "SMS_NUMBER",
                "value": "5055014735"
            },
            {
                "name": "NOTIFICATION_ID",
                "value": "Ecom.AcctMgmt.VMReset"
            },
            {
                "name": "TEMPORARY_VOICE_MAIL_PIN",
                "value": "1234"
            },
            {
                "name": "VOICE_MAIL_PLATFORM",
                "value": "LCTL"
            },
            {
                "name": "EXT_TRACKING_NUM",
                "value": "RX891889900"
            },
            {
                "name": "SCRNR_ID",
                "value": "rxmicr03"
            }
        ]
    }




testcases = []
# 1. Valid payload
tc1 = copy.deepcopy(base_payload)
testcases.append(tc1)

# 2. RequestId is mandatory
tc2 = copy.deepcopy(base_payload)
tc2["requestId"] = ""
testcases.append(tc2)

# 3. MessageSrcSystem is mandatory
tc3 = copy.deepcopy(base_payload)
tc3["messageSrcSystem"] = ""
testcases.append(tc3)

# 4. NotificationReason is mandatory
tc4 = copy.deepcopy(base_payload)
tc4["notificationReason"] = ""
testcases.append(tc4)

# 5. BillingSource should be CRIS or C2E or ENSEMBLE : case1: invalid BillingSource
tc5 = copy.deepcopy(base_payload)
for attr in tc5["dataAttributes"]:
    if attr["name"] == "BILLING_SOURCE":
        attr["value"] = "INVALID_SOURCE"
        break
testcases.append(tc5)

# 6. BillingSource should be CRIS or C2E or ENSEMBLE : case2: empty BillingSource
tc6 = copy.deepcopy(base_payload)
for attr in tc6["dataAttributes"]:
    if attr["name"] == "BILLING_SOURCE":
        attr["value"] = ""
        break
testcases.append(tc6)

# 7. BAN should not be empty
tc7 = copy.deepcopy(base_payload)
for attr in tc7["dataAttributes"]:
    if attr["name"] == "BAN":
        attr["value"] = ""
        break
testcases.append(tc7)

# 8. EmailAddress & SMSAddress both should not  be empty: case1: empty EmailAddress
tc8 = copy.deepcopy(base_payload)
for attr in tc8["dataAttributes"]:
    if attr["name"] == "CUST_EMAIL_ADDRESS":
        attr["value"] = ""
        break
testcases.append(tc8)

# 9. EmailAddress & SMSAddress both should not  be empty: case2: both empty
tc9 = copy.deepcopy(base_payload)
for attr in tc9["dataAttributes"]:
    if attr["name"] == "CUST_EMAIL_ADDRESS":
        attr["value"] = ""
    if attr["name"] == "SMS_NUMBER":
        attr["value"] = ""
testcases.append(tc9)

# 10. NotificationID should not be empty
tc9 = copy.deepcopy(base_payload)
for attr in tc9["dataAttributes"]:
    if attr["name"] == "NOTIFICATION_ID":
        attr["value"] = ""
        break
testcases.append(tc9)

# 11. If BillingSource='C2E' , BAN should not empty
tc10 = copy.deepcopy(base_payload)
for attr in tc10["dataAttributes"]:
    if attr["name"] == "BILLING_SOURCE":
        attr["value"] = "C2E"
    if attr["name"] == "BAN":
        attr["value"] = ""
testcases.append(tc10)

# 12. Company should be either 'LQ' or 'LCTL' : case1: invalid Company
tc11 = copy.deepcopy(base_payload)
for attr in tc11["dataAttributes"]:
    if attr["name"] == "COMPANY":
        attr["value"] = "INVALID_COMPANY"
        break
testcases.append(tc11)

# 13. Company should be either 'LQ' or 'LCTL' : case2: empty Company
tc12 = copy.deepcopy(base_payload)
for attr in tc12["dataAttributes"]:
    if attr["name"] == "COMPANY":
        attr["value"] = ""
        break
testcases.append(tc12)

# 14. If Company is 'LCTL' , BAN should not be empty
tc13 = copy.deepcopy(base_payload)
for attr in tc13["dataAttributes"]:
    if attr["name"] == "COMPANY":
        attr["value"] = "LCTL"
    if attr["name"] == "BAN":
        attr["value"] = ""
testcases.append(tc13)

# 15. TemporaryVoicemailPIN should not empty
tc14 = copy.deepcopy(base_payload)
for attr in tc14["dataAttributes"]:
    if attr["name"] == "TEMPORARY_VOICE_MAIL_PIN":
        attr["value"] = ""
        break
testcases.append(tc14)

# 16. VoicemailPlatform should be equal to 'LQ' or 'LCTL' : case1: invalid VoicemailPlatform
tc15 = copy.deepcopy(base_payload)
for attr in tc15["dataAttributes"]:
    if attr["name"] == "VOICE_MAIL_PLATFORM":
        attr["value"] = "INVALID_PLATFORM"
        break
testcases.append(tc15)

# 17. VoicemailPlatform should be equal to 'LQ' or 'LCTL' : case2: empty VoicemailPlatform
tc16 = copy.deepcopy(base_payload)
for attr in tc16["dataAttributes"]:
    if attr["name"] == "VOICE_MAIL_PLATFORM":
        attr["value"] = ""
        break
testcases.append(tc16)

# 18. exttrackingnum should not be empty if Company='LQ'
tc17 = copy.deepcopy(base_payload)
for attr in tc17["dataAttributes"]:
    if attr["name"] == "COMPANY":
        attr["value"] = "LQ"
    if attr["name"] == "EXT_TRACKING_NUM":
        attr["value"] = ""
testcases.append(tc17)

# 19. Exclude if Name is empty or length is less than 2
tc18 = copy.deepcopy(base_payload)
for attr in tc18["dataAttributes"]:
    if attr["name"] == "CUSTOMER_CONTACT_NAME":
        attr["value"] = "A"
testcases.append(tc18)

# 20. scrnrid should not be empty
tc19 = copy.deepcopy(base_payload)
for attr in tc19["dataAttributes"]:
    if attr["name"] == "SCRNR_ID":
        attr["value"] = ""
        break
testcases.append(tc19)

#

# api_urls = [
#     "https://ntfwf-ordering-service-test1.rke-odc-test.corp.intranet/api/notification/order/config"
# ]
