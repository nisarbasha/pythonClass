mainid = input("Enter the main id")

if mainid == "yes":
    sid = input("Enter the id")
    if sid == "yes":
        sysid = input("Enter the sysid")
        if sysid == "yes":
            print("Login working")
        else:
            print("sysid not found")
    else:
        print("id not found")
else:
    print("mainid not found")

