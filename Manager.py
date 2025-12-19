user_exists = []
log = {

}
day = 0
with open("log.txt", "r") as file:
    lines = file.readlines()
    i = 0
    for l in lines:
        if i == 0:
            name = l.strip().split(";")
            user_exists = name
            i += 1
            continue
        s = l.strip().split(";")
        v = [s[1],s[2],s[3]]
        log[s[0]] = v
        day += 1
        

def option_One(option):
    if option == "Set":
        print("--------------------------")
        print("Please Enter Your Name")
        name = input()
        print("Please Enter Your Fitness Goal:")
        print("1. Fat Loss")
        print("2. Muscle Gain")
        print("3. Endurance")
        print("4. General Fitness")
        valid_option = False
        choice = 0
        while not valid_option:
            try:
                input_String = input()
                choice = int(input_String)
                if choice > 4 or choice < 1:
                    print("Please Enter a valid Number")
                    continue
                valid_option = True
            except ValueError: 
                print("Please Enter a valid Number")
        if choice == 1:
            return [name, "Fat Loss"]
        elif choice == 2:
            return [name, "Muscle Gain"]
        elif choice == 3:
            return [name, "Endurance"]
        else:
            return [name, "General Fitness"]
    else:
        print("--------------------------")
        print("Please Enter Your Fitness Goal:")
        print("1. Fat Loss")
        print("2. Muscle Gain")
        print("3. Endurance")
        print("4. General Fitness")
        valid_option = False
        choice = 0
        while not valid_option:
            try:
                input_String = input()
                choice = int(input_String)
                if choice > 4 or choice < 1:
                    print("Please Enter a valid Number")
                    continue
                valid_option = True
            except ValueError: 
                print("Please Enter a valid Number")
        if choice == 1:
            return "Fat Loss"
        elif choice == 2:
            return "Muscle Gain"
        elif choice == 3:
            return "Endurance"
        else:
            return "General Fitness"
def option_Two():
    global day
    valid_option = False
    workout = ""
    while not valid_option:
        try: 
            print("--------------------------")
            print("Please Enter Workout In This Format")
            print("type:minutes:intensity")
            print("Intensity can be Low, Medium, High")
            workout = input()
            workout = workout.split(":")
            workout [1] = int(workout[1])
            workout [2] = workout[2].lower()
            if workout [1] < 0:
                print("Add Proper Minutes")
                continue
            if  workout[2] == "low" or workout[2] == "high" or workout[2]== "medium":
                day += 1
                log[f"Day:{day}"] = workout
                print("Added Workout")
                return
            else: 
                print("Please enter proper intensity")
                continue
        except (ValueError, IndexError):
            print("Error Occured: Please try again")
def option_Three():
    global day
    if day == 0:
        print("No logs added cannot do this process")
        return
    print("--------------------------")
    print("Here is the complete Log")
    for key, value in log.items():
        print(f"{key}, Workout Info: Type: {value[0]}, Time: {value[1]}, Intensity: {value[2]}")
    return
def option_Four():
    Intensity_types = {

    }
    workout_types = {
    }   
    global day
    if day == 0:
        print("No logs added cannot do this process")
        return
    time_total = 0
    for key, value in log.items():
        time_total += int(value[1])
        if value[0] not in workout_types:
            workout_types[value[0]] = int(value[1])
        else:
            workout_types[value[0]] += int(value[1])
        if value[2] not in Intensity_types:
            Intensity_types[value[2]] = 1
        else:
            Intensity_types[value[2]] += 1
    average_time = time_total / day
    print("--------------------------")
    print("Here is your analysis:")
    print(f"Total Workout Time: {time_total}")
    print(f"Total Average Time Per Day: {int(average_time)}")
    print(f"Workout Type and Total Time:")
    for key, value in workout_types.items():
        print(f"Workout Type: {key}, Time: {value}")
    print(f"Intensity and count:")
    for key, value in Intensity_types.items():
        print(f"Intensity Type: {key}, Count: {value}")
    return

def option_Five():
    global day
    if day == 0:
        print("No logs added cannot do this process")
        return
    high_intensity = set()
    print("Here are the days you did well:")
    for key, value in log.items():
        if(value[2] == "high"):
            high_intensity.add(f"{key}, Workout Info: Type: {value[0]}, Time: {value[1]}, Intensity: {value[2]}")
        if(int(value[1]) > 60):
            high_intensity.add(f"{key}, Workout Info: Type: {value[0]}, Time: {value[1]}, Intensity: {value[2]}")
    print("--------------------------")        
    for value in high_intensity:
        print(value)
    return


while True:
    print("--------------------------")
    print("Welcome to Fitness Manager")
    print("Please Select Your Choice:")
    print("Option 1: Set / Update Profile")
    print("Option 2: Add Workout Log (for a day)")
    print("Option 3: View All Logs")
    print("Option 4: Analyze Logs")
    print("Option 5: Show Systematic logs")
    print("Option 6: Reset All Data")
    print("Option 7: Exit")
    print("Please Enter A Number:")
    valid_option = False
    choice = 0
    while not valid_option:
        try:
            input_String = input()
            choice = int(input_String)
            if choice > 7 or choice < 1:
                print("Please Enter a valid Number")
                continue
            valid_option = True
        except ValueError: 
            print("Please Enter a valid Number")
    if choice == 1:
        if not user_exists: 
            user_exists = option_One("Set")
        else: 
            print(f"Current Info: Name: {user_exists[0]}, Level: {user_exists[1]}")
            user_exists[1] = option_One("Update")
    elif choice == 2:
        option_Two()
    elif choice == 3:
        option_Three()
    elif choice == 4:
        option_Four()
    elif choice == 5:
        option_Five()
    elif choice == 6:
        log = {

        }
        day = 0
        print("Reset Data Complete")
    elif choice == 7:
        with open("log.txt", "w") as file:
            file.write(f"{user_exists[0]};{user_exists[1]}" + "\n")
            for key,value in log.items():
                file.write(f"{key};{value[0]};{value[1]};{value[2]}" + "\n")
        break
print("Thank You For Visiting")
