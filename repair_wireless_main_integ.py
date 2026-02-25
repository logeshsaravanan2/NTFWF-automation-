def generate_testcases(base_payload):
    import copy

    testcase_descriptions = [
            "1. valid payload",
            "2. RequestId is mandatory",
            "3. MessageSrcSystem is mandatory",
            "4. NotificationReason is mandatory",
            "5. BillingSource should be CRIS or C2E or ENSEMBLE : case1: invalid BillingSource",
            "6. BillingSource should be CRIS or C2E or ENSEMBLE : case2: empty BillingSource",
            "7. BAN should not be empty",
            "8. EmailAddress & SMSAddress both should not  be empty: case1: empty EmailAddress",
            "10. NotificationID should not be empty",
            "11. Company should not be empty",
            "12. SSID should not be empty",
            "13. PASS_PHRASE should not be empty",
            "14. EXT_TRACKING_NUM should not be empty",
            "15. SCRNR_ID should not be empty"
    ]
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


    # 10. NotificationID should not be empty
    tc10 = copy.deepcopy(base_payload)
    for attr in tc10["dataAttributes"]:
        if attr["name"] == "NOTIFICATION_ID":
            attr["value"] = ""
            break
    testcases.append(tc10)

    # 11. Company should not be empty
    tc11 = copy.deepcopy(base_payload)
    for attr in tc11["dataAttributes"]:
        if attr["name"] == "COMPANY":
            attr["value"] = ""
            break
    testcases.append(tc11)

    # 12. SSID should not be empty
    tc12 = copy.deepcopy(base_payload)
    for attr in tc12["dataAttributes"]:
        if attr["name"] == "SSID":
            attr["value"] = ""
            break
    testcases.append(tc12)

    # 13. PASS_PHRASE should not be empty
    tc13 = copy.deepcopy(base_payload)
    for attr in tc13["dataAttributes"]:
        if attr["name"] == "PASS_PHRASE":
            attr["value"] = ""
            break
    testcases.append(tc13)

    # 14. EXT_TRACKING_NUM should not be empty
    tc14 = copy.deepcopy(base_payload)
    for attr in tc14["dataAttributes"]:
        if attr["name"] == "EXT_TRACKING_NUM":
            attr["value"] = ""
            break
    testcases.append(tc14)

    # 15. SCRNR_ID should not be empty
    tc15 = copy.deepcopy(base_payload)
    for attr in tc15["dataAttributes"]:
        if attr["name"] == "SCRNR_ID":
            attr["value"] = ""
            break
    testcases.append(tc15)
    for idx, tc in enumerate(testcases):
        tc["description"] = testcase_descriptions[idx]

    return testcases
