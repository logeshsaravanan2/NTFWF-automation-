from ship_conf_new import testcase_descriptions


def generate_testcases(base_payload):
    import copy
    testcase_descriptions=[
        "1. Valid payload",
        "2. Request ID is mandatory",
        "3. MessageSourceSystem is mandatory",
        "4. TEMPLATE should be ECOM.ORDERING.SHIPPINGCONF",
        "5. Notification Stack should be mandatory",
        "6. BAN or BAID should be present - both missing",
        "7. BAN length should not be less than 9",
        "8. UPSTrackingNumber is mandatory",
        "9. OrderDate is mandatory",
        "10. DeliveryDate is mandatory",
        "11. ShippingName is mandatory",
        "12. ActualShipDate is mandatory",
        "13. Shipping Address1 or ShipCity or ShipState or ShipZip – one of the should be present - all missing",
        "14. Shipping Address1 or ShipCity or ShipState or ShipZip – one of the should be present - one missing (ShipState)",
        "15. Company should be equal to “LCTL”",
        "16. MarketType should be either “I” or “S”"
    ]
    testcases = []
    # 1. Valid payload
    tc1 = copy.deepcopy(base_payload)
    testcases.append(tc1)

    # 2. Request ID is mandatory
    tc2 = copy.deepcopy(base_payload)
    tc2["requestId"] = ""
    testcases.append(tc2)

    #3. MessageSourceSystem is mandatory
    tc3 = copy.deepcopy(base_payload)
    tc3["messageSrcSystem"] = ""
    testcases.append(tc3)

    # 4. TEMPLATE should be ECOM.ORDERING.SHIPPINGCONF
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

    #8. UPSTrackingNumber is mandatory
    tc8 = copy.deepcopy(base_payload)
    for attr in tc8["dataAttributes"]:
        if attr["name"] == "UPS_TRACKING_NUMBER":
            attr["value"] = ""
            break
    testcases.append(tc8)

    #9. OrderDate is mandatory
    tc9 = copy.deepcopy(base_payload)
    for attr in tc9["dataAttributes"]:
        if attr["name"] == "ORDER_DATE":
            attr["value"] = ""
            break
    testcases.append(tc9)
    #10. DeliveryDate is mandatory
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
    # 13. Shipping Address1 or ShipCity or ShipState or ShipZip – one of the should be present - all missing
    tc13 = copy.deepcopy(base_payload)
    for attr in tc13["dataAttributes"]:
        if attr["name"] == "SHIPPING_ADDRESS1":
            attr["value"] = ""
        if attr["name"] == "SHIP_CITY":
            attr["value"] = ""
        if attr["name"] == "SHIP_STATE":
            attr["value"] = ""
        if attr["name"] == "SHIP_ZIP":
            attr["value"] = ""
    testcases.append(tc13)

    #14. Shipping Address1 or ShipCity or ShipState or ShipZip – one of the should be present - one missing (ShipState)
    tc14 = copy.deepcopy(base_payload)
    for attr in tc14["dataAttributes"]:
        if attr["name"] == "SHIPPING_ADDRESS1":
            attr["value"] = "123 Main St"
        if attr["name"] == "SHIP_CITY":
            attr["value"] = "Anytown"
        if attr["name"] == "SHIP_STATE":
            attr["value"] = ""
        if attr["name"] == "SHIP_ZIP":
            attr["value"] = "12345"
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
        if attr["name"] == "MARKET_TYPE":
            attr["value"] = "X"
            break
    testcases.append(tc16)
    for idx, tc in enumerate(testcases):
        tc["description"] = testcase_descriptions[idx]

    return testcases
