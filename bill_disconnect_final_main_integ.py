from ship_conf_new import testcase_descriptions


# "{
#     ""requestId"": ""BM_1755097478697"",
#     ""sendTimeStamp"": ""2025-12-03T14:59:38.697"",
#     ""messageSrcSystem"": ""BMPS"",
#     ""notificationReason"": ""ECOM.BILLING.DISCONNECTFINALBILL"",
#     ""dataAttributes"": [
#         {
#             ""name"": ""NOTIFICATION_ID"",
#             ""value"": ""1755097478697""
#         },
#         {
#             ""name"": ""TEMPLATE"",
#             ""value"": ""ECOM.BILLING.DISCONNECTFINALBILL""
#         },
#         {
#             ""name"": ""NOTIFYING_APP"",
#             ""value"": ""BMPS""
#         },
#         {
#             ""name"": ""NOTIFYING_MODULE"",
#             ""value"": ""BMPS""
#         },
#         {
#             ""name"": ""BAN"",
#             ""value"": ""330971197""
#         },
#         {
#             ""name"": ""ORDER_ID"",
#             ""value"": ""1023186386""
#         },
#         {
#             ""name"": ""AUTOPAY"",
#             ""value"": """"
#         },
#         {
#             ""name"": ""AUTO_MAINTENANCE"",
#             ""value"": """"
#         },
#         {
#             ""name"": ""LANGUAGE"",
#             ""value"": ""ENGLISH""
#         },
#         {
#             ""name"": ""CUSTOMER_TYPE"",
#             ""value"": ""I""
#         },
#         {
#             ""name"": ""DO_NOT_NOTIFY"",
#             ""value"": ""false""
#         },
#         {
#             ""name"": ""MDU"",
#             ""value"": ""false""
#         },
#         {
#             ""name"": ""PAPERLESS_BILLING"",
#             ""value"": ""false""
#         },
#         {
#             ""name"": ""WINBACK"",
#             ""value"": ""False""
#         },
#         {
#             ""name"": ""ORDERSOURCETYPE"",
#             ""value"": ""QFMigration""
#         },
#         {
#             ""name"": ""CUST_DONOT_EMAIL"",
#             ""value"": ""false""
#         },
#         {
#             ""name"": ""CUST_EMAIL_ADDRESS"",
#             ""value"": ""Tadi.DhanaSuryaRajaSekharReddy@lumen.com""
#         },
#         {
#             ""name"": ""CUST_EMAIL_INVALID"",
#             ""value"": ""false""
#         },
#         {
#             ""name"": ""SMS_NUMBER"",
#             ""value"": ""9702705840""
#         },
#         {
#             ""name"": ""CUSTOMER_SMS_INVALID"",
#             ""value"": ""false""
#         },
#         {
#             ""name"": ""BILL_OPTIN_EMAIL"",
#             ""value"": ""Y""
#         },
#         {
#             ""name"": ""BILL_OPTIN_SMS"",
#             ""value"": ""Y""
#         },
#         {
#             ""name"": ""ORDE_OPTIN_EMAIL"",
#             ""value"": ""Y""
#         },
#         {
#             ""name"": ""DISPATCH_REQUIRED"",
#             ""value"": ""false""
#         },
#         {
#             ""name"": ""REPA_OPTIN_EMAIL"",
#             ""value"": ""Y""
#         },
#         {
#             ""name"": ""ADDRESS_ID"",
#             ""value"": """"
#         },
#         {
#             ""name"": ""FIRST_NAME"",
#             ""value"": ""SURYA""
#         },
#         {
#             ""name"": ""LAST_NAME"",
#             ""value"": ""REDDY""
#         },
#         {
#             ""name"": ""NAME_ID"",
#             ""value"": """"
#         },
#         {
#             ""name"": ""ORDER_CREATE_DATE"",
#             ""value"": ""20250813145055""
#         },
#         {
#             ""name"": ""ORDER_DUE_DATE"",
#             ""value"": ""20250813""
#         },
#         {
#             ""name"": ""ORDER_TYPE"",
#             ""value"": ""DC""
#         },
#         {
#             ""name"": ""SERVICE_ADDRESS"",
#             ""value"": ""7056 MEADE ST, WELLINGTON, CO, 80549""
#         },
#         {
#             ""name"": ""ATTRIBUTE_GROUP"",
#             ""value"": ""SERVICE_GROUP=HSI~SERVICE_STATUS=DC~LAST_ACTION_RSN_CD=INITIAL ACTIVATION""
#         },
#         {
#             ""name"": ""HSIONORDER"",
#             ""value"": ""true""
#         },
#         {
#             ""name"": ""PRISMONORDER"",
#             ""value"": ""false""
#         },
#         {
#             ""name"": ""COMPANY"",
#             ""value"": ""LCTL""
#         },
#         {
#             ""name"": ""BILL_CYCLE_DATE"",
#             ""value"": """"
#         },
#         {
#             ""name"": ""PRODUCT_ID"",
#             ""value"": ""9705684749""
#         }
#     ]
# }"

def generate_testcases(base_payload):
    import copy

    testcase_descriptions=[
        "1. When all mandatory fields are present.",
        "2. Validation of mandatory fields (When requestId is blank)",
        "3. Validation of mandatory fields (When messageSrcSystem is blank)",
        "4. Validation of mandatory fields (When notificationReason is null)",
        "5. Validation of mandatory fields (When TEMPLATE is missing or empty)",
        "6. When BAN is missing or empty in the payload",
        "7. When BAN is not equal to 9 digits.",
        "8. When Company  value is not equal to  “LCTL” or “LQ”",
        "9. When OrderId is empty or missing",
        "10. When MDU flag is true.",
        "11. When CUSTOMERTYPE  value is not equal to  “I” or missing",
        "12. When CUST_EMAIL_ADDRESS is present & SMS_NUMBER is empty",
        "13. When SMS_NUMBER is present & CUST_EMAIL_ADDRESS is empty",
        "14. When SMS_NUMBER is empty & CUST_EMAIL_ADDRESS is empty",
        "15. When SMS_NUMBER is present & CUST_EMAIL_ADDRESS is present",
        "16. When CUSTOMER_SMS_INVALID is false & CUST_EMAIL_INVALID is  true",
        "17. When CUSTOMER_SMS_INVALID is true & CUST_EMAIL_INVALID is  false",
        "18. When CUSTOMER_SMS_INVALID is false & CUST_EMAIL_INVALID is  false",
        "19. When CUSTOMER_SMS_INVALID is true & CUST_EMAIL_INVALID is  true",
        "20. When CUST_DONOT_EMAIL is true",
        "21. when messageSrcSystem is not BMPS",
        "22. When NotificationReason is not same as Template",
        "23. When Company  value is missing or blank",
        "24. MDU flag is Missing or null.",
        "25. When CUSTOMERTYPE  value is missing or null",
        "26. When BILL_OPTIN_EMAIL is N  & BILL_OPTIN_SMS is Y",
        "27. When BILL_OPTIN_SMS is N  & BILL_OPTIN_EMAIL  is Y",
        "28.When BILL_OPTIN_SMS is N  & BILL_OPTIN_EMAIL  is N",
        "29. When BILL_OPTIN_SMS is  Y & BILL_OPTIN_EMAIL  is  Y"
    ]

    testcases = []

    # 1. When all mandatory fields are present.
    tc1 = copy.deepcopy(base_payload)
    testcases.append(tc1)

    # 2. Validation of mandatory fields (When requestId is blank)
    tc2 = copy.deepcopy(base_payload)
    tc2["messageSrcSystem"] = ""
    testcases.append(tc2)

    # 3. Validation of mandatory fields (When messageSrcSystem is blank)
    tc3 = copy.deepcopy(base_payload)
    tc3["messageSrcSystem"] = ""
    testcases.append(tc3)

    #     4. Validation of mandatory fields (When notificationReason is null)
    tc4 = copy.deepcopy(base_payload)
    tc4["notificationReason"] = ""
    testcases.append(tc4)

    #     5. Validation of mandatory fields (When TEMPLATE is missing or empty)
    tc5 = copy.deepcopy(base_payload)
    for attr in tc5["dataAttributes"]:
        if attr["name"] == "TEMPLATE":
            attr["value"] = ""
            break
    testcases.append(tc5)

    #     6. When BAN is missing or empty in the payload
    tc6 = copy.deepcopy(base_payload)
    for attr in tc6["dataAttributes"]:
        if attr["name"] == "BAN":
            attr["value"] = ""
            break
    testcases.append(tc6)

    #     7. When BAN is not equal to 9 digits.
    tc7 = copy.deepcopy(base_payload)
    for attr in tc7["dataAttributes"]:
        if attr["name"] == "BAN":
            attr["value"] = "123456"
            break
    testcases.append(tc7)

    #     8. When Company  value is not equal to  “LCTL” or “LQ”
    tc8 = copy.deepcopy(base_payload)
    for attr in tc8["dataAttributes"]:
        if attr["name"] == "COMPANY":
            attr["value"] = "XXXX"
            break
    testcases.append(tc8)

    #     9. When OrderId is empty or missing
    tc9 = copy.deepcopy(base_payload)
    for attr in tc9["dataAttributes"]:
        if attr["name"] == "ORDER_ID":
            attr["value"] = ""
            break
    testcases.append(tc9)

    #     10. When MDU flag is true.
    tc10 = copy.deepcopy(base_payload)
    for attr in tc10["dataAttributes"]:
        if attr["name"] == "MDU":
            attr["value"] = "true"
            break
    testcases.append(tc10)

    #     11. When CUSTOMERTYPE  value is not equal to  “I” or missing
    tc11 = copy.deepcopy(base_payload)
    for attr in tc11["dataAttributes"]:
        if attr["name"] == "CUSTOMER_TYPE":
            attr["value"] = "X"
            break
    testcases.append(tc11)

    #     12. When CUST_EMAIL_ADDRESS is present & SMS_NUMBER is empty
    tc12 = copy.deepcopy(base_payload)
    for attr in tc12["dataAttributes"]:
        if attr["name"] == "CUST_EMAIL_ADDRESS":
            attr["value"] = "Tadi.DhanaSuryaRajaSekharReddy@lumen.com"
        if attr["name"] == "SMS_NUMBER":
            attr["value"] = ""
    testcases.append(tc12)

    #     13. When SMS_NUMBER is present & CUST_EMAIL_ADDRESS is empty
    tc13 = copy.deepcopy(base_payload)
    for attr in tc13["dataAttributes"]:
        if attr["name"] == "CUST_EMAIL_ADDRESS":
            attr["value"] = ""
        if attr["name"] == "SMS_NUMBER":
            attr["value"] = "1234567890"
    testcases.append(tc13)

    #     14. When SMS_NUMBER is empty & CUST_EMAIL_ADDRESS is empty
    tc14 = copy.deepcopy(base_payload)
    for attr in tc14["dataAttributes"]:
        if attr["name"] == "CUST_EMAIL_ADDRESS":
            attr["value"] = ""
        if attr["name"] == "SMS_NUMBER":
            attr["value"] = ""
    testcases.append(tc14)

    #     15. When SMS_NUMBER is present & CUST_EMAIL_ADDRESS is present
    tc15 = copy.deepcopy(base_payload)
    for attr in tc15["dataAttributes"]:
        if attr["name"] == "CUST_EMAIL_ADDRESS":
            attr["value"] = "Tadi.DhanaSuryaRajaSekharReddy@lumen.com"
        if attr["name"] == "SMS_NUMBER":
            attr["value"] = "1234567890"
    testcases.append(tc15)

    #     16. When CUSTOMER_SMS_INVALID is false & CUST_EMAIL_INVALID is  true
    tc16 = copy.deepcopy(base_payload)
    for attr in tc16["dataAttributes"]:
        if attr["name"] == "CUST_EMAIL_INVALID":
            attr["value"] = "true"
        if attr["name"] == "CUSTOMER_SMS_INVALID":
            attr["value"] = "false"
    testcases.append(tc16)

    #     17. When CUSTOMER_SMS_INVALID is true & CUST_EMAIL_INVALID is  false
    tc17 = copy.deepcopy(base_payload)
    for attr in tc17["dataAttributes"]:
        if attr["name"] == "CUST_EMAIL_INVALID":
            attr["value"] = "false"
        if attr["name"] == "CUSTOMER_SMS_INVALID":
            attr["value"] = "true"
    testcases.append(tc17)

    #     18. When CUSTOMER_SMS_INVALID is false & CUST_EMAIL_INVALID is  false
    tc18 = copy.deepcopy(base_payload)
    for attr in tc18["dataAttributes"]:
        if attr["name"] == "CUST_EMAIL_INVALID":
            attr["value"] = "false"
        if attr["name"] == "CUSTOMER_SMS_INVALID":
            attr["value"] = "false"
    testcases.append(tc18)

    #     19. When CUSTOMER_SMS_INVALID is true & CUST_EMAIL_INVALID is  true
    tc19 = copy.deepcopy(base_payload)
    for attr in tc19["dataAttributes"]:
        if attr["name"] == "CUST_EMAIL_INVALID":
            attr["value"] = "true"
        if attr["name"] == "CUSTOMER_SMS_INVALID":
            attr["value"] = "true"
    testcases.append(tc19)

    #     20. When CUST_DONOT_EMAIL is true
    tc20 = copy.deepcopy(base_payload)
    for attr in tc20["dataAttributes"]:
        if attr["name"] == "CUST_DONOT_EMAIL":
            attr["value"] = "true"
            break
    testcases.append(tc20)

    #     21. when messageSrcSystem is not BMPS
    tc21 = copy.deepcopy(base_payload)
    tc21["messageSrcSystem"] = "XXXX"
    testcases.append(tc21)

    #     22. When NotificationReason is not same as Template
    tc22 = copy.deepcopy(base_payload)
    tc22["notificationReason"] = "XXXX"
    testcases.append(tc22)

    #     23. When Company  value is missing or blank
    tc23 = copy.deepcopy(base_payload)
    for attr in tc23["dataAttributes"]:
        if attr["name"] == "COMPANY":
            attr["value"] = ""
            break
    testcases.append(tc23)

    #     24. When MDU flag is Missing or null.
    tc24 = copy.deepcopy(base_payload)
    for attr in tc24["dataAttributes"]:
        if attr["name"] == "MDU":
            attr["value"] = ""
            break
    testcases.append(tc24)

    #     25. When CUSTOMERTYPE  value is missing or null
    tc25 = copy.deepcopy(base_payload)
    for attr in tc25["dataAttributes"]:
        if attr["name"] == "CUSTOMER_TYPE":
            attr["value"] = ""
            break
    testcases.append(tc25)

    #     26. When BILL_OPTIN_EMAIL is N  & BILL_OPTIN_SMS is Y
    tc26 = copy.deepcopy(base_payload)
    for attr in tc26["dataAttributes"]:
        if attr["name"] == "BILL_OPTIN_EMAIL":
            attr["value"] = "N"
        if attr["name"] == "BILL_OPTIN_SMS":
            attr["value"] = "Y"
    testcases.append(tc26)

    #     27. When BILL_OPTIN_SMS is N  & BILL_OPTIN_EMAIL  is Y
    tc27 = copy.deepcopy(base_payload)
    for attr in tc27["dataAttributes"]:
        if attr["name"] == "BILL_OPTIN_EMAIL":
            attr["value"] = "Y"
        if attr["name"] == "BILL_OPTIN_SMS":
            attr["value"] = "N"
    testcases.append(tc27)

    #     28.When BILL_OPTIN_SMS is N  & BILL_OPTIN_EMAIL  is N
    tc28 = copy.deepcopy(base_payload)
    for attr in tc28["dataAttributes"]:
        if attr["name"] == "BILL_OPTIN_EMAIL":
            attr["value"] = "N"
        if attr["name"] == "BILL_OPTIN_SMS":
            attr["value"] = "N"
    testcases.append(tc28)

    #     29. When BILL_OPTIN_SMS is  Y & BILL_OPTIN_EMAIL  is  Y
    tc29 = copy.deepcopy(base_payload)
    for attr in tc29["dataAttributes"]:
        if attr["name"] == "BILL_OPTIN_EMAIL":
            attr["value"] = "Y"
        if attr["name"] == "BILL_OPTIN_SMS":
            attr["value"] = "Y"
    testcases.append(tc29)

    for idx, tc in enumerate(testcases):
        tc["description"] = testcase_descriptions[idx]

    return testcases