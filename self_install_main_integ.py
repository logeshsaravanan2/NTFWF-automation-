
def generate_testcases(base_payload):
    import copy

    testcase_descriptions = [
        "1. Valid payload",
        "2. Missing requestId",
        "3. Invalid requestId prefix",
        "4. Invalid MessageSourceSystem",
        "5. Empty DispatchReason",
        "6. Invalid DispatchReason",
        "7. Empty DueDate",
        "8. Empty NotificationId",
        "9. Empty NotificationStack",
        "10. Empty Company",
        "11. Empty CustomerType",
        "12. Invalid CustomerType",
        "13. Empty OrderNumber",
        "14. template name invalid"
    ]
    testcases = []
    # 1. Valid payload
    tc1 = copy.deepcopy(base_payload)
    testcases.append(tc1)

    # 2.RequestId is mandatory and should be started with “CLICK”, case1: Missing requestId
    tc2 = copy.deepcopy(base_payload)
    tc2["requestId"] = ""
    testcases.append(tc2)

    #3. RequestId is mandatory and should be started with “CLICK”, case2: starts with invalid prefix
    tc3 = copy.deepcopy(base_payload)
    tc3["requestId"] = "INVALID_1744898400386"
    testcases.append(tc3)

    # 4.MessageSourceSystem must be “CLICK”.
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
    for attr in tc8["dataAttributes"]:
        if attr["name"] == "NOTIFICATION_ID":
            attr["value"] = ""
            break
    testcases.append(tc8)

    # 9. “NotificationStack” should not be empty.
    tc9 = copy.deepcopy(base_payload)
    for attr in tc9["dataAttributes"]:
        if attr["name"] == "NOTIFICATION_STACK":
            attr["value"] = ""
            break
    testcases.append(tc9)

    # 10. Company should not be empty.
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

    # 14. Template name should be valid.
    tc14 = copy.deepcopy(base_payload)
    for attr in tc14["dataAttributes"]:
        if attr["name"] == "TEMPLATE":
            attr["value"] = "INVALID_TEMPLATE"
            break
    testcases.append(tc14)

    for idx, tc in enumerate(testcases):
        tc["description"] = testcase_descriptions[idx]

    return testcases
