# Electric Usage Function
def elec_usage(unit):
    usage = 0
    fee = 0
    unit_left = float(unit)

    if int(unit) > 150:
        fee = 28.22
        convert_limit = [150, 250, 400]
        convert = [3.2484, 4.2218, 4.4217]

    else:
        fee = 8.19
        convert_limit = [15, 10, 10, 65, 50, 250, 400]
        convert = [2.3488, 2.9882, 3.2405, 3.6237, 3.7171, 4.2218, 4.4217]

    for x in range(len(convert_limit)):
        if convert_limit[x] <= 400:
            if unit_left - convert_limit[x] > 0:
                unit_left = unit_left - convert_limit[x]
                usage = usage + (convert_limit[x] * convert[x])
            else:
                usage = usage + (unit_left * convert[x])
                break
        else:
            usage = usage + (convert_limit * convert[x])
            break

    usage = float(usage) + fee

    return usage


# Main Function
while exit != 1:
    print("")
    name = input("Enter your name : ")
    unit = input("Enter Electricity Unit : ")

    fee = 0.2048
    ft_fee = float(unit) * float(fee)

    elec = elec_usage(unit)

    vat_percent = 0.07
    vat = (ft_fee + elec) * vat_percent

    payment = ft_fee + elec + vat
    print("")
    print(f"Name : {name}")
    print(f"Usage Unit : {unit}")
    print("Cost : %.2f THB" % payment)
    print("")
    exit_prompt = input('type "exit" to exit the program : ')

    if exit_prompt.lower() == "exit":
        print("Thank you :)")
        exit = 1
    else:
        exit = 0
