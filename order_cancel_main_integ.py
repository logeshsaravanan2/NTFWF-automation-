# "{
#     ""requestId"": ""BM_1749489486297"",
#     ""sendTimeStamp"": ""2025-11-18T17:01:25.96"",
#     ""messageSrcSystem"": ""BMPS"",
#     ""notificationReason"": ""ECOM.ORDERING.CANCELLED"",
#     ""dataAttributes"": [
#         {
#             ""name"": ""NOTIFICATION_ID"",
#             ""value"": ""1749489486297""
#         },
#         {
#             ""name"": ""TEMPLATE"",
#             ""value"": ""ECOM.ORDERING.CANCELLED""
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
#             ""name"": ""ORDER_TYPE"",
#             ""value"": ""DC""
#         },
#         {
#             ""name"": ""DISCONNECT_RSN_Code"",
#             ""value"": ""Y""
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
#             ""value"": ""500124930""
#         },
#         {
#             ""name"": ""ORDER_ID"",
#             ""value"": ""1022770561""
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
#             ""name"": ""CUSTOMER_TYPE"",
#             ""value"": ""S""
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
#             ""value"": ""true""
#         },
#         {
#             ""name"": ""WINBACK"",
#             ""value"": ""False""
#         },
#         {
#             ""name"": ""ORDER_SOURCE_TYPE"",
#             ""value"": ""EASE""
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
#             ""value"": """"
#         },
#         {
#             ""name"": ""PRODUCT_ID"",
#             ""value"": ""2525860103""
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
#             ""name"": ""DISPATCH_WINDOW"",
#             ""value"": """"
#         },
#         {
#             ""name"": ""name_ID"",
#             ""value"": """"
#         },
#         {
#             ""name"": ""ORDER_CREATE_DATE"",
#             ""value"": ""11-18-2025""
#         },
#         {
#             ""name"": ""ORDER_DUE_DATE"",
#             ""value"": ""11-29-2025""
#         },
#         {
#             ""name"": ""ORN"",
#             ""value"": ""ORN-25060965418730798""
#         },
#         {
#             ""name"": ""SERVICE_ADDRESS"",
#             ""value"": ""148 W SUMMERWOOD RD, LITTLETON, NC, 27850""
#         },
#         {
#             ""name"": ""ATTRIBUTE_GROUP"",
#             ""value"": ""SERVICE_GROUP=VOICE, HSI~SERVICE_STATUS=CA~LAST_ACTION_RSN_CD=INITIAL ACTIVATION""
#         },
#         {
#             ""name"": ""HSI_ON_ORDER"",
#             ""value"": ""true""
#         },
#         {
#             ""name"": ""PRISM_ON_ORDER"",
#             ""value"": ""false""
#         },
#         {
#             ""name"": ""BILL_RECORD_ONLY_IND"",
#             ""value"": ""false""
#         },
#         {
#             ""name"": ""LANGUAGE"",
#             ""value"": ""ENGLISH""
#         },
#         {
#             ""name"": ""MARKET"",
#             ""value"": ""CHANGE""
#         },
#         {
#             ""name"": ""CUSTOMER_SMS_INVALID"",
#             ""value"": ""false""
#         },
#         {
#             ""name"": ""ORDE_OPTIN_EMAIL"",
#             ""value"": ""Y""
#         },
#         {
#             ""name"": ""WFM_JOB_CODE"",
#             ""value"": """"
#         },
#         {
#             ""name"": ""ORDE_OPTIN_SMS"",
#             ""value"": ""Y""
#         },
#         {
#             ""name"": ""APPT_FROM_DATE"",
#             ""value"": """"
#         },
#         {
#             ""name"": ""APPT_TO_DATE"",
#             ""value"": """"
#         },
#         {
#             ""name"": ""DISPATCH_REQUIRED"",
#             ""value"": ""false""
#         },
#         {
#             ""name"": ""BILLING_ADDRESS"",
#             ""value"": ""148 W SUMMERWOOD RD, LITTLETON, NC, 27850""
#         },
#         {
#             ""name"": ""COMPANY"",
#             ""value"": ""LCTL""
#         },
#         {
#             ""name"": ""RETAIL_MODEM_PICKUP"",
#             ""value"": """"
#         },
#         {
#             ""name"": ""MODEM_SHIPPED"",
#             ""value"": ""true""
#         },
#         {
#             ""name"": ""MOVE_DISCONNECT_DATE"",
#             ""value"": """"
#         },
#         {
#             ""name"": ""USO_ORDER_NUMBER"",
#             ""value"": """"
#         }
#     ]
# }"

def generate_testcases(base_payload):
    import copy

    testcase_descriptions = [
        "1. When all mandatory fields are present.",
        "2. Validation of mandatory fields (When messageSrcSystem is missing)",
        "3. Validation of mandatory fields (When requestId is empty)",
        "4. Validation of mandatory fields When notificationReason is null",
        "5. Validation of mandatory fields When TEMPLATE is missing or empty",
        "6. NotificationReason is not same as Template",
        "7. When CustomerType other than“S” or “I” or empty & missing",
        "8. when BAN is less then 9 or empty",
        "9. When BAN is missing",
        "10. When MDU flag is true.",
        "11. When Market value is  “B”",
        "12. billRecordsOnlyInd is true",
        "13. When Company  value is not equal to  “LCTL” or “LQ”or blank",
        "14. when Language other than “ENGLISH” or BLANK or Missing",
        "15. when OrderType is not equals to “DC\" or empty",
        "16. When dataAttributes is empty or don’t have any data in dataAttributes",
        "17. When BAN is above 9",
        "18. when Company is missing",
        "19. If OrderType equals to “DC” then Disconnect_RSN_Code equal to one of these – “R\",\"DE\",\"U\",\"SBI\",\"N”",
        "20. when OrderType is equals to “DC\", &  Disconnect_RSN_Code should not be one of these – “R\",\"DE\",\"U\",\"SBI\",\"N”",
        "21. When all mandatory fields are present and CUSTOMER_TYPE is 'S'"
    ]

    testcases = []
    # 1. When all mandatory fields are present.
    tc1 = copy.deepcopy(base_payload)
    testcases.append(tc1)

    # 2. Validation of mandatory fields (When messageSrcSystem is missing)
    tc2 = copy.deepcopy(base_payload)
    tc2["messageSrcSystem"] = ""
    testcases.append(tc2)

    # 3. Validation of mandatory fields (When requestId is empty)
    tc3 = copy.deepcopy(base_payload)
    tc3["requestId"] = ""
    testcases.append(tc3)

    # 4. Validation of mandatory fields When notificationReason is null
    tc4 = copy.deepcopy(base_payload)
    tc4["notificationReason"] = None
    testcases.append(tc4)

    # 5. Validation of mandatory fields When TEMPLATE is missing or empty
    tc5 = copy.deepcopy(base_payload)
    for attr in tc5["dataAttributes"]:
        if attr["name"] == "TEMPLATE":
            attr["value"] = ""
            break
    testcases.append(tc5)

    # 6. NotificationReason is not same as Template
    tc6 = copy.deepcopy(base_payload)
    tc6["notificationReason"] = "ECOM.ORDERING.CREATED"
    testcases.append(tc6)

    # 7. When CustomerType other than“S” or “I” or empty & missing
    tc7 = copy.deepcopy(base_payload)
    for attr in tc7["dataAttributes"]:
        if attr["name"] == "CUSTOMER_TYPE":
            attr["value"] = "X"
            break
    testcases.append(tc7)

    # 8. when BAN is less then 9 or empty
    tc8 = copy.deepcopy(base_payload)
    for attr in tc8["dataAttributes"]:
        if attr["name"] == "BAN":
            attr["value"] = "12345"
            break
    testcases.append(tc8)

    # 9. When BAN is missing
    tc9 = copy.deepcopy(base_payload)
    for attr in tc9["dataAttributes"]:
        if attr["name"] == "BAN":
            attr["value"] = ""
            break
    testcases.append(tc9)

    # 10. When MDU flag is true.
    tc10 = copy.deepcopy(base_payload)
    for attr in tc10["dataAttributes"]:
        if attr["name"] == "MDU":
            attr["value"] = "true"
            break
    testcases.append(tc10)

    # 11. When Market value is  “B”
    tc11 = copy.deepcopy(base_payload)
    for attr in tc11["dataAttributes"]:
        if attr["name"] == "MARKET":
            attr["value"] = "B"
            break
    testcases.append(tc11)

    # 12. billRecordsOnlyInd is true
    tc12 = copy.deepcopy(base_payload)
    for attr in tc12["dataAttributes"]:
        if attr["name"] == "BILL_RECORD_ONLY_IND":
            attr["value"] = "true"
            break
    testcases.append(tc12)

    # 13. When Company  value is not equal to  “LCTL” or “LQ”or blank
    tc13 = copy.deepcopy(base_payload)
    for attr in tc13["dataAttributes"]:
        if attr["name"] == "COMPANY":
            attr["value"] = "XYZ"
            break
    testcases.append(tc13)

    # 14. when Language other than “ENGLISH” or BLANK or Missing
    tc14 = copy.deepcopy(base_payload)
    for attr in tc14["dataAttributes"]:
        if attr["name"] == "LANGUAGE":
            attr["value"] = "SPANISH"
            break
    testcases.append(tc14)

    # 15. when OrderType is not equals to “DC" or empty
    tc15 = copy.deepcopy(base_payload)
    for attr in tc15["dataAttributes"]:
        if attr["name"] == "ORDER_TYPE":
            attr["value"] = "XX"
            break
    testcases.append(tc15)

    # 16. When dataAttributes is empty or don’t have any data in dataAttributes
    tc16 = copy.deepcopy(base_payload)
    tc16["dataAttributes"] = []
    testcases.append(tc16)

    # 17. When BAN is above 9
    tc17 = copy.deepcopy(base_payload)
    for attr in tc17["dataAttributes"]:
        if attr["name"] == "BAN":
            attr["value"] = "5001249301"
            break
    testcases.append(tc17)

    # 18. when Company is missing
    tc18 = copy.deepcopy(base_payload)
    for attr in tc18["dataAttributes"]:
        if attr["name"] == "COMPANY":
            attr["value"] = ""
            break
    testcases.append(tc18)

    # 19. If OrderType equals to “DC” then Disconnect_RSN_Code equal to one of these – “R","DE","U","SBI","N"
    tc19 = copy.deepcopy(base_payload)
    for attr in tc19["dataAttributes"]:
        if attr["name"] == "DISCONNECT_RSN_Code":
            attr["value"] = "X"
            break
    testcases.append(tc19)

    # 20. when OrderType is equals to “DC", &  Disconnect_RSN_Code should not be one of these – “R","DE","U","SBI","N"
    tc20 = copy.deepcopy(base_payload)
    for attr in tc20["dataAttributes"]:
        if attr["name"] == "DISCONNECT_RSN_Code":
            attr["value"] = ""
            break
    testcases.append(tc20)

    # 21. When all mandatory fields are present and CUSTOMER_TYPE is 'S'
    tc21 = copy.deepcopy(base_payload)
    for attr in tc21["dataAttributes"]:
        if attr["name"] == "CUSTOMER_TYPE":
            attr["value"] = "S"
            break
    testcases.append(tc21)

    for idx, tc in enumerate(testcases):
        tc["description"] = testcase_descriptions[idx]

    return testcases