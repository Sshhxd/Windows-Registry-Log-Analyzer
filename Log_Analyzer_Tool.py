# ------------------------------- IMPORTS ---------------------------------


# ------------------------------ VARIABLES --------------------------------
file_path = r"" # -------------------------------------------------------------> Add the path to your file

# ----------------------------- DICTIONARIES ------------------------------


# --------------------------- PARSING FUNCTIONS ---------------------------

def check_file(file_path): # --------------------> Verifies that the file actually exists / has contents.
    try:
        with open(file_path, "r") as Checking:
            if not Checking.read().strip():
                return False
            print("File is valid")
            return True

    except FileNotFoundError:
        print("File missing or empty")
        return False
    

def parse_log(file_path):
    Create_Key_Counts = {}

    with open(file_path, "r") as Reading:
        for line in Reading: # -------------------> Reads through each line of the file to look for the keyword 'Key:'.
            
            if "Key:" in line:
                Keyparts = line.split()
                Reg_Key = Keyparts[-1] # ----------------> Take out the last part of each line, in this case it is the registry key path.
            

            # --> Reads through each line of the file to look for the keyword 'Creating or opening the key.'.
            if "Creating or opening the key." in line:
                Parts = line.split()
                time1 = Parts[0]    # --> Variable 'time1' gets the same value as the first part of 'Reg_key_Create' or 'Date'.
                time2 = Parts[1]    # --> Variable 'time2' gets the same value as the second part of 'Reg_key_Create' or 'Time'.
            
                timestamp = f"{time1} {time2}" # --> Variable 'timestamp' puts 'Date' and 'Time' together in one string. ("Date Time").


            # --> Add / append 'timestamp' + 'Reg_Key' to the dictionary 'Create_Key_Counts'.
            if 'timestamp' in locals() and 'Reg_Key' in locals():
                if (timestamp, Reg_Key) in Create_Key_Counts:
                    Create_Key_Counts[(timestamp, Reg_Key)] += 1
                else:
                    Create_Key_Counts[(timestamp, Reg_Key)] = 1

    return Create_Key_Counts


def print_results(results): # -----------------------------------------------------> Creates the desired printing format.
    # --> This part checks if the character lenght of each line is longer than 95.
    for (timestamp, Reg_Key), count in results.items():
        print(f"{timestamp} -> {Reg_Key} ({count} times)")

        #LENGTH = len(f"{timestamp} -> {Reg_Key} ({count} times)")
        #if LENGTH > 95:
        #    print("Is longer than 95 chars: " f"{timestamp} -> {Reg_Key} ({count} times)")
        #    print("Longer than 95 characters :", len(f"{timestamp} -> {Reg_Key} ({count} times)"))
        #else:
        #    print("Is shorter than 95 chars: " f"{timestamp} -> {Reg_Key} ({count} times)")
        #    print("Shorter than 95 characters :", len(f"{timestamp} -> {Reg_Key} ({count} times)"))


if check_file(file_path):
    results = parse_log(file_path)
    print_results(results)
else:
    print("File missing or empty")


    # This part checks if the character lenght of each line is longer than 95.
    #LENGTH = len(f"{Reg_key_Create} -> {Reg_Key} ({count} times)")
    #if LENGTH > 95:
    #    print("Longer than 95 characters :", len(f"{Reg_key_Create} -> {Reg_Key} ({count} times)"))
    #else:
    #    print("Shorter than 95 characters :", len(f"{Reg_key_Create} -> {Reg_Key} ({count} times)"))

    # Final print line which you see in your output console.
