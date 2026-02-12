Create_Key_Counts = {}
Reg_Key_Counts = {}


with open("log.txt") as Read:
    lines = Read.readlines()
    
    for each in lines:
        if "Key:" in each:
            Keyparts = each.split()
            Reg_Key = Keyparts[-1]


        if "Creating or opening the key." in each:
            parts = each.split()
            Reg_key_Create = parts[0] + parts[1]    # Date / Time

            String = Reg_key_Create
            String = each.split()
            time1 = String[0]
            time2 = String[1]


            if Reg_key_Create in Create_Key_Counts: 
                Create_Key_Counts[(Reg_key_Create, Reg_Key)] += 1
            else:
                Create_Key_Counts[(Reg_key_Create, Reg_Key)] = 1
                
                        
    
for (Reg_key_Create, Reg_Key), count in Create_Key_Counts.items():
    LENGTH = len(f"{Reg_key_Create} -> {Reg_Key} ({count} times)")
    if LENGTH > 95:
        print("Longer than 95 characters :", len(f"{Reg_key_Create} -> {Reg_Key} ({count} times)"))
    else:
        print("Shorter than 95 characters :", len(f"{Reg_key_Create} -> {Reg_Key} ({count} times)"))

    print(f"{time1} {time2} -> {Reg_Key} ({count} times)")
print("\n\n\n")
