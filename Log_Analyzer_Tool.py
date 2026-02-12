# ----------------------------- DICTIONARIES -----------------------------
Create_Key_Counts = {}

# ----------------------------- PARSING LOGIC -----------------------------
with open("log.txt") as Read:    # Change "log.txt" to your specific file name under the same directory.
    lines = Read.readlines()

    # Reads through each line of the file to look for the keyword 'Key:'.
    for each in lines:
        if "Key:" in each:
            Keyparts = each.split()
            Reg_Key = Keyparts[-1]    # Take out the last part of each line, in this case it is the registry key path.

        
         # Reads through each line of the file to look for the keyword 'Creating or opening the key.'.
        if "Creating or opening the key." in each:
            parts = each.split()
            Reg_key_Create = parts[0] + parts[1]    # Take out the first part of each line; Date / Time

            # 1. This next part takes 'Reg_key_Create' which is the date and time.
            # 2. Variable 'time1' gets the same value as the first part of 'Reg_key_Create' 
            # 3. Variable 'time2' gets the same value as the second part of 'Reg_key_Create' 
            String = Reg_key_Create
            String = each.split()
            time1 = String[0]    # Date
            time2 = String[1]    # Time
            
            # Add / append 'Reg_key_Create' + 'Reg_Key' to the dictionary 'Create_Key_Counts'
            if Reg_key_Create in Create_Key_Counts: 
                Create_Key_Counts[(Reg_key_Create, Reg_Key)] += 1
            else:
                Create_Key_Counts[(Reg_key_Create, Reg_Key)] = 1
                
                        
# This part contains the print() logic.
# This can and will be improved later on-
for (Reg_key_Create, Reg_Key), count in Create_Key_Counts.items():
    
    # This part checks if the character lenght of each line is longer than 95.
    LENGTH = len(f"{Reg_key_Create} -> {Reg_Key} ({count} times)")
    if LENGTH > 95:
        print("Longer than 95 characters :", len(f"{Reg_key_Create} -> {Reg_Key} ({count} times)"))
    else:
        print("Shorter than 95 characters :", len(f"{Reg_key_Create} -> {Reg_Key} ({count} times)"))

    # Final print line which you see in your output console.
    print(f"{time1} {time2} -> {Reg_Key} ({count} times)")
