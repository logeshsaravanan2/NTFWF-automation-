def generate_testcases(base_payload):
    import copy
    testcase_descriptions = [
        "1. Valid payload",
        "2. request id is mandatory",
        "3. request id starts with BMOM",
        "4. messageSrcSystem should be BMOM",
        "5. ban should be 9 digits",
        "6. notification id should be ECOM.Ordering.VacationSuspend",
        "7. one of the email or sms should be present - case 1: both missing",
        "8. one of the email or sms should be present - case 2: only email missing",
        "9. one of the email or sms should be present - case 3: only sms missing",
        "10. product tn should be 10 digits",
        "11. product details should be POTS or HSI or HSI,POTS - case 1: null",
        "12. product details should be POTS or HSI or HSI,POTS - case 2: HSI only",
        "13. product details should be POTS or HSI or HSI,POTS - case 3: POTS only",
        "14. product details should be POTS or HSI or HSI,POTS - case 4: POTS,HSI",
        "15. company should be LQ or CTL - case 1: CTL",
        "16. company should be LQ or CTL - case 2: LQ",
        "17. company should be LQ or CTL - case 3: invalid value",
        "18. service address city should not be empty",
        "19. service address state should not be empty",
        "20. service address zip should not be empty",
        "21. order number should not be empty",
        "22. service address line1 should not be empty",
        "23. order type should not be empty",
        "24. market should be I - case 1: valid",
        "25. market should be I - case 2: invalid",
        "26. order create date should be in YYYYMMDD format - case 1: valid",
        "27. order create date should be in YYYYMMDD format - case 2: invalid",
        "28. order create date should be in YYYYMMDD format - case 3: empty",
        "29. order due date should be in MM-DD-YYYY format - case 1: valid",
        "30. order due date should be in MM-DD-YYYY format - case 2: invalid",
        "31. order due date should be in MM-DD-YYYY format - case 3: empty"


    ]
    testcases = []
    # 1. Valid payload
    tc1 = copy.deepcopy(base_payload)
    testcases.append(tc1)

    # 2. request id is mandatory
    tc2 = copy.deepcopy(base_payload)
    tc2["requestId"] = ""
    testcases.append(tc2)

    # 3.request id starts with BMOM
    tc3 = copy.deepcopy(base_payload)
    tc3["requestId"] = "XYZ12345"
    testcases.append(tc3)

    # 4. messageSrcSystem should be BMOM
    tc4 = copy.deepcopy(base_payload)
    tc4["messageSrcSystem"] = "OTHER"
    testcases.append(tc4)

    # 5. ban should be 9 digits
    tc5 = copy.deepcopy(base_payload)
    for attr in tc5["dataAttributes"]:
        if attr["name"] == "BAN":
            attr["value"] = "12345"
    testcases.append(tc5)

    # 6. notification id should be ECOM.Ordering.VacationSuspend
    tc6 = copy.deepcopy(base_payload)
    for attr in tc6["dataAttributes"]:
        if attr["name"] == "NOTIFICATION_ID":
            attr["value"] = "VacationSuspend"
    testcases.append(tc6)

    # 7. one of the email or sms should be present - case 1: both missing
    tc7 = copy.deepcopy(base_payload)
    for attr in tc7["dataAttributes"]:
        if attr["name"] == "CUST_EMAIL_ADDRESS":
            attr["value"] = ""
        if attr["name"] == "SMS_NUMBER":
            attr["value"] = ""
    testcases.append(tc7)

    # 8. one of the email or sms should be present - case 2: only email missing
    tc8 = copy.deepcopy(base_payload)
    for attr in tc8["dataAttributes"]:
        if attr["name"] == "CUST_EMAIL_ADDRESS":
            attr["value"] = ""
    testcases.append(tc8)

    # 9. one of the email or sms should be present - case 3: only sms missing
    tc9 = copy.deepcopy(base_payload)
    for attr in tc9["dataAttributes"]:
        if attr["name"] == "SMS_NUMBER":
            attr["value"] = ""
    testcases.append(tc9)

    #10. product tn should be 10 digits
    tc10 = copy.deepcopy(base_payload)
    for attr in tc10["dataAttributes"]:
        if attr["name"] == "PRODUCT_TN":
            attr["value"] = "123456"
    testcases.append(tc10)

    #11. product details should be POTS or HSI or HSI,POTS - case 1: null
    tc11 = copy.deepcopy(base_payload)
    for attr in tc11["dataAttributes"]:
        if attr["name"] == "PRODUCT_DETAIL":
            attr["value"] = ""
    testcases.append(tc11)

    #12. product details should be POTS or HSI or HSI,POTS - case 2: HSI only
    tc12 = copy.deepcopy(base_payload)
    for attr in tc12["dataAttributes"]:
        if attr["name"] == "PRODUCT_DETAIL":
            attr["value"] = "HSI"
    testcases.append(tc12)

    #13. product details should be POTS or HSI or HSI,POTS - case 3: POTS only
    tc13 = copy.deepcopy(base_payload)
    for attr in tc13["dataAttributes"]:
        if attr["name"] == "PRODUCT_DETAIL":
            attr["value"] = "POTS"
    testcases.append(tc13)

    #14. product details should be POTS or HSI or HSI,POTS - case 4: POTS,HSI
    tc14 = copy.deepcopy(base_payload)
    for attr in tc14["dataAttributes"]:
        if attr["name"] == "PRODUCT_DETAIL":
            attr["value"] = "POTS,HSI"
    testcases.append(tc14)

    #     15. company should be LQ or CTL - case 1: CTL
    tc15 = copy.deepcopy(base_payload)
    for attr in tc15["dataAttributes"]:
        if attr["name"] == "COMPANY":
            attr["value"] = "CTL"
    testcases.append(tc15)

    #16. company should be LQ or CTL - case 2: LQ
    tc16 = copy.deepcopy(base_payload)
    for attr in tc16["dataAttributes"]:
        if attr["name"] == "COMPANY":
            attr["value"] = "LQ"
    testcases.append(tc16)

    # 17. company should be LQ or CTL - case 3: invalid value
    tc17 = copy.deepcopy(base_payload)
    for attr in tc17["dataAttributes"]:
        if attr["name"] == "COMPANY":
            attr["value"] = "XYZ"
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

    # 22. service address line1 should not be empty
    tc22 = copy.deepcopy(base_payload)
    for attr in tc22["dataAttributes"]:
        if attr["name"] == "SERVICE_ADDRESS_LINE1":
            attr["value"] = ""
    testcases.append(tc22)

    # 23. order type should not be empty
    tc23 = copy.deepcopy(base_payload)
    for attr in tc23["dataAttributes"]:
        if attr["name"] == "ORDER_TYPE":
            attr["value"] = ""
    testcases.append(tc23)

    # 24.  market should be I - case 1: valid
    tc24 = copy.deepcopy(base_payload)
    for attr in tc24["dataAttributes"]:
        if attr["name"] == "MARKET":
            attr["value"] = "I"
    testcases.append(tc24)

    # 25.  market should be I - case 2: invalid
    tc25 = copy.deepcopy(base_payload)
    for attr in tc25["dataAttributes"]:
        if attr["name"] == "MARKET":
            attr["value"] = "X"
    testcases.append(tc25)

    # 26. order create date should be in YYYYMMDD format - case 1: valid
    tc26 = copy.deepcopy(base_payload)
    for attr in tc26["dataAttributes"]:
        if attr["name"] == "ORDER_CREATE_DATE":
            attr["value"] = "20250220"
    testcases.append(tc26)

    # 27. order create date should be in YYYYMMDD format - case 2: invalid
    tc27 = copy.deepcopy(base_payload)
    for attr in tc27["dataAttributes"]:
        if attr["name"] == "ORDER_CREATE_DATE":
            attr["value"] = "20-02-2025"
    testcases.append(tc27)

    # 28. order create date should be in YYYYMMDD format - case 3: empty
    tc28 = copy.deepcopy(base_payload)
    for attr in tc28["dataAttributes"]:
        if attr["name"] == "ORDER_CREATE_DATE":
            attr["value"] = ""
    testcases.append(tc28)

    # 29. order due date should be in MM-DD-YYYY format - case 1: valid
    tc29 = copy.deepcopy(base_payload)
    for attr in tc29["dataAttributes"]:
        if attr["name"] == "ORDER_DUE_DATE":
            attr["value"] = "07-21-2025"
    testcases.append(tc29)

    # 30. order due date should be in MM-DD-YYYY format - case 2: invalid
    tc30 = copy.deepcopy(base_payload)
    for attr in tc30["dataAttributes"]:
        if attr["name"] == "ORDER_DUE_DATE":
            attr["value"] = "2025/07/21"
    testcases.append(tc30)

    # 31. order due date should be in MM-DD-YYYY format - case 3: empty
    tc31 = copy.deepcopy(base_payload)
    for attr in tc31["dataAttributes"]:
        if attr["name"] == "ORDER_DUE_DATE":
            attr["value"] = ""
    testcases.append(tc31)

    for idx, tc in enumerate(testcases):
        tc["description"] = testcase_descriptions[idx]

    return testcases