# "{
# ""requestId"": ""BM_1746466025628"",
# ""sendTimeStamp"": ""2025-11-06T17:27:05.626"",
# ""messageSrcSystem"": ""BMPS"",
# ""notificationReason"": ""ECOM.ORDERING.CONFDISCONNECT"",
# ""dataAttributes"": [
#     {
#         ""name"": ""NOTIFICATION_ID"",
# ""value"": ""1746466025632""
# },
# {
#     ""name"": ""TEMPLATE"",
# ""value"": ""ECOM.ORDERING.CONFDISCONNECT""
# },
# {
#     ""name"": ""FIRST_NAME"",
# ""value"": ""SURYA""
# },
# {
#     ""name"": ""LAST_NAME"",
# ""value"": ""REDDY""
# },
# {
#     ""name"": ""ORDER_TYPE"",
# ""value"": ""DC""
# },
# {
#     ""name"": ""DISCONNECT_RSN_Code"",
# ""value"": ""A""
# },
# {
#     ""name"": ""NOTIFYING_APP"",
# ""value"": ""BMPS""
# },
# {
#     ""name"": ""NOTIFYING_MODULE"",
# ""value"": ""BMPS""
# },
# {
#     ""name"": ""BAN"",
# ""value"": ""332267508""
# },
# {
#     ""name"": ""ORDER_ID"",
# ""value"": ""1022641765""
# },
# {
#     ""name"": ""AUTOPAY"",
# ""value"": """"
#         },
#         {
#             ""name"": ""AUTO_MAINTENANCE"",
#             ""value"": """"
# },
# {
#     ""name"": ""CUSTOMER_TYPE"",
# ""value"": ""S""
# },
# {
#     ""name"": ""DO_NOT_NOTIFY"",
# ""value"": ""false""
# },
# {
#     ""name"": ""MDU"",
# ""value"": ""false""
# },
# {
#     ""name"": ""PAPERLESSBILLING"",
# ""value"": ""true""
# },
# {
#     ""name"": ""WINBACK"",
# ""value"": ""False""
# },
# {
#     ""name"": ""ORDER_SOURCE_TYPE"",
# ""value"": ""ESHOP-Customer Care""
# },
# {
#     ""name"": ""CUST_EMAIL_ADDRESS"",
# ""value"": ""Tadi.DhanaSuryaRajaSekharReddy@lumen.com""
# },
# {
#     ""name"": ""CUST_EMAIL_INVALID"",
# ""value"": ""false""
# },
# {
#     ""name"": ""SMS_NUMBER"",
# ""value"": ""7209858712""
# },
# {
#     ""name"": ""PRODUCT_ID"",
# ""value"": ""4356889114""
# },
# {
#     ""name"": ""REPA_OPTIN_EMAIL"",
# ""value"": ""Y""
# },
# {
#     ""name"": ""ADDRESS_ID"",
# ""value"": """"
#         },
#         {
#             ""name"": ""DISPATCH_WINDOW"",
#             ""value"": """"
# },
# {
#     ""name"": ""NAME_ID"",
# ""value"": """"
#         },
#         {
#             ""name"": ""ORDER_CREATE_DATE"",
#             ""value"": ""12-18-2025""
#         },
#         {
#             ""name"": ""ORDER_DUE_DATE"",
#             ""value"": ""12-22-2025""
#         },
#         {
#             ""name"": ""ORN"",
#             ""value"": ""ORN-25050578921688052""
#         },
#         {
#             ""name"": ""SERVICE_ADDRESS"",
#             ""value"": ""2772 S 2170 E, SAINT GEORGE, UT, 84790""
#         },
#         {
#             ""name"": ""ATTRIBUTE_GROUP"",
#             ""value"": ""SERVICE_GROUP=HSI~SERVICE_STATUS=DC~LAST_ACTION_RSN_CD=INITIAL ACTIVATION""
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
#             ""value"": """"
# },
# {
#     ""name"": ""LANGUAGE"",
# ""value"": ""ENGLISH""
# },
# {
#     ""name"": ""MARKET"",
# ""value"": ""DISCONNECT""
# },
# {
#     ""name"": ""CUSTOMER_SMS_INVALID"",
# ""value"": ""true""
# },
# {
#     ""name"": ""ORDE_OPTIN_EMAIL"",
# ""value"": ""Y""
# },
# {
#     ""name"": ""WFM_JOB_CODE"",
# ""value"": """"
#         },
#         {
#             ""name"": ""ORDE_OPTIN_SMS"",
#             ""value"": ""Y""
#         },
#         {
#             ""name"": ""APPT_FROM_DATE"",
#             ""value"": """"
# },
# {
#     ""name"": ""APPT_TO_DATE"",
# ""value"": """"
#         },
#         {
#             ""name"": ""DISPATCH_REQUIRED"",
#             ""value"": ""false""
#         },
#         {
#             ""name"": ""BILLING_ADDRESS"",
#             ""value"": ""2772 S 2170 E, SAINT GEORGE, UT, 84790""
#         },
#         {
#             ""name"": ""COMPANY"",
#             ""value"": ""LCTL""
#         },
#         {
#             ""name"": ""RETAIL_MODEM_PICKUP"",
#             ""value"": """"
# },
# {
#     ""name"": ""MODEM_SHIPPED"",
# ""value"": ""false""
# },
# {
#     ""name"": ""MOVE_DISCONNECT_DATE"",
# ""value"": """"
#         },
#         {
#             ""name"": ""USO_ORDER_NUMBER"",
#             ""value"": """"
# }
# ]
# }"

def generate_testcases(base_payload):
    import copy

    testcase_descriptions = [
        "1. When all mandatory fields are present.",
        "2. Validation of mandatory fields (When  requestId is empty)",
        "3.Validation of mandatory fields (When  is notificationReason missing)",
        "4. Validation of mandatory fields When  messageSrcSystem is null",
        "5. Validation of mandatory fields When TEMPLATE is missing or empty",
        "6. Template =”ECOM.ORDERING.CONFDISCONNECT” , verify Either Email or SMS on of them should be valid and opted in.",
        "7. When CustomerType other than“S” or “I” or empty & missing",
        "8. when BAN not equal to 9 or empty",
        "9. When MDU flag is true.",
        "10. When Market value is  “B”",
        "11. billRecordsOnlyInd is true",
        "12. When Company  value is not equal to  “LCTL” or “LQ”or blank",
        "13. when Language other than “ENGLISH”or BLANK or Missing",
        "14. when OrderType is not equals to “DC" or "empty",
        "15. When dataAttributes is empty or don’t have any data in dataAttributes",
        "16. When Company is missing",
        "17. when OrderType is equals to “DC", "&  Disconnect_RSN_Code should not be one of these – “R","DE","U","SBI","N",
        "18. when OrderType is equals to “DC", "&  Disconnect_RSN_Code equal to be one of these – “R","DE","U","SBI","N",
        "19.  When BAN is missing",
        "20. When all mandatory fields are present and CUSTOMER_TYPE is 'S'"
    ]

    testcases = []

    # 1. When all mandatory fields are present.
    tc1 = copy.deepcopy(base_payload)
    testcases.append(tc1)

    # 2. Validation of mandatory fields (When  requestId is empty)
    tc2 = copy.deepcopy(base_payload)
    tc2["requestId"] = ""
    testcases.append(tc2)

    # 3.Validation of mandatory fields (When  is notificationReason missing)
    tc3 = copy.deepcopy(base_payload)
    tc3["notificationReason"] = ""
    testcases.append(tc3)

    # 4. Validation of mandatory fields When  messageSrcSystem is null
    tc4 = copy.deepcopy(base_payload)
    tc4["messageSrcSystem"] = ""
    testcases.append(tc4)

    # 5. Validation of mandatory fields When TEMPLATE is missing or empty
    tc5 = copy.deepcopy(base_payload)
    for attr in tc5["dataAttributes"]:
        if attr["name"] == "TEMPLATE":
            attr["value"] = ""
            break
    testcases.append(tc5)

    # 6. Template =”ECOM.ORDERING.CONFDISCONNECT” , verify Either Email or SMS on of them should be valid and opted in.
    tc6 = copy.deepcopy(base_payload)
    for attr in tc6["dataAttributes"]:
        if attr["name"] == "CUST_EMAIL_INVALID":
            attr["value"] = "true"
        if attr["name"] == "CUSTOMER_SMS_INVALID":
            attr["value"] = "true"
        if attr["name"] == "ORDE_OPTIN_EMAIL":
            attr["value"] = "N"
        if attr["name"] == "ORDE_OPTIN_SMS":
            attr["value"] = "N"
    testcases.append(tc6)

    # 7. When CustomerType other than“S” or “I” or empty & missing
    tc7 = copy.deepcopy(base_payload)
    for attr in tc7["dataAttributes"]:
        if attr["name"] == "CUSTOMER_TYPE":
            attr["value"] = "X"
    testcases.append(tc7)

    # 8. when BAN not equal to 9 or empty
    tc8 = copy.deepcopy(base_payload)
    for attr in tc8["dataAttributes"]:
        if attr["name"] == "BAN":
            attr["value"] = "12345"
            break
    testcases.append(tc8)


    # 9. When MDU flag is true.
    tc9 = copy.deepcopy(base_payload)
    for attr in tc9["dataAttributes"]:
        if attr["name"] == "MDU":
            attr["value"] = "true"
            break
    testcases.append(tc9)

    # 10. When Market value is  “B”
    tc10 = copy.deepcopy(base_payload)
    for attr in tc10["dataAttributes"]:
        if attr["name"] == "MARKET":
            attr["value"] = "B"
            break
    testcases.append(tc10)

    # 11. billRecordsOnlyInd is true
    tc11 = copy.deepcopy(base_payload)
    for attr in tc11["dataAttributes"]:
        if attr["name"] == "BILL_RECORD_ONLY_IND":
            attr["value"] = "true"
            break
    testcases.append(tc11)

    # 12. When Company  value is not equal to  “LCTL” or “LQ”or blank
    tc12 = copy.deepcopy(base_payload)
    for attr in tc12["dataAttributes"]:
        if attr["name"] == "COMPANY":
            attr["value"] = "XYZ"
            break
    testcases.append(tc12)

    # 13. when Language other than “ENGLISH”or BLANK or Missing
    tc13 = copy.deepcopy(base_payload)
    for attr in tc13["dataAttributes"]:
        if attr["name"] == "LANGUAGE":
            attr["value"] = "SPANISH"
            break
    testcases.append(tc13)

    # 14. when OrderType is not equals to “DC" or empty
    tc14 = copy.deepcopy(base_payload)
    for attr in tc14["dataAttributes"]:
        if attr["name"] == "ORDER_TYPE":
            attr["value"] = "XX"
            break
    testcases.append(tc14)

    # 15. When dataAttributes is empty or don’t have any data in dataAttributes
    tc15 = copy.deepcopy(base_payload)
    tc15["dataAttributes"] = []
    testcases.append(tc15)

    # 16. When Company is missing
    tc16 = copy.deepcopy(base_payload)
    for attr in tc16["dataAttributes"]:
        if attr["name"] == "COMPANY":
            attr["value"] = ""
            break
    testcases.append(tc16)

    # 17. when OrderType is equals to “DC", &  Disconnect_RSN_Code should not be one of these – “R","DE","U","SBI","N"
    tc17 = copy.deepcopy(base_payload)
    for attr in tc17["dataAttributes"]:
        if attr["name"] == "DISCONNECT_RSN_Code":
            attr["value"] = "A"
            break
    testcases.append(tc17)

    #18. when OrderType is equals to “DC", &  Disconnect_RSN_Code equal to be one of these – “R","DE","U","SBI","N"
    tc18 = copy.deepcopy(base_payload)
    for attr in tc18["dataAttributes"]:
        if attr["name"] == "DISCONNECT_RSN_Code":
            attr["value"] = "R"
            break
    testcases.append(tc18)

    # 19.  When BAN is missing
    tc19 = copy.deepcopy(base_payload)
    for attr in tc8["dataAttributes"]:
            if attr["name"] == "BAN":
                attr["value"] = ""
            break
    testcases.append(tc19)

    # 20. When all mandatory fields are present and CUSTOMER_TYPE is 'S'
    tc20 = copy.deepcopy(base_payload)
    for attr in tc20["dataAttributes"]:
        if attr["name"] == "CUSTOMER_TYPE":
            attr["value"] = "S"
            break
    testcases.append(tc20)

    for idx, tc in enumerate(testcases):
        tc["description"] = testcase_descriptions[idx]

    return testcases