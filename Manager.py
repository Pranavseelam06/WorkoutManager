import json

user_exists = {

}
log = []

day = 0
with open("log.json", "r") as file:
    lines = json.load(file)
    user_exists = lines["profile"]
    log = lines["logs"]
    day = int(log[-1]["day"])
        

def option_One(option):
    if option == "Set":
        print("--------------------------")
        print("Please Enter Your Name")
        name = input()
        user_exists["name"] = name
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
            user_exists["goal"] = "Fat Loss"
        elif choice == 2:
            user_exists["goal"] = "Muscle Gain"
        elif choice == 3:
            user_exists["goal"] = "Endurance"
        else:
            user_exists["goal"] = "General Fitness"
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
            user_exists["goal"] = "Fat Loss"
        elif choice == 2:
            user_exists["goal"] = "Muscle Gain"
        elif choice == 3:
            user_exists["goal"] = "Endurance"
        else:
            user_exists["goal"] = "General Fitness"
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
            workout_dict = {

            }
            workout = input()
            workout = workout.split(":")
            workout [1] = int(workout[1])
            workout [2] = workout[2].lower()
            if workout [1] < 0:
                print("Add Proper Minutes")
                continue
            if  workout[2] == "low" or workout[2] == "high" or workout[2]== "medium":
                day += 1
                workout_dict["day"] = day
                workout_dict["type"] = workout[0].lower()
                workout_dict["minutes"] = int(workout[1])
                workout_dict["intensity"] = workout[2]
                log.append(workout_dict)
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
    for line in log:
        print(f"Day: {line['day']}, Workout Info: Type: {line['type']}, Time: {line['minutes']}, Intensity: {line['intensity']}")
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
    for line in log:
        time_total += int(line["minutes"])
        if line["type"] not in workout_types:
            workout_types[line["type"]] = int(line["minutes"])
        else:
            workout_types[line["type"]] += int(line["minutes"])
        if line["intensity"] not in Intensity_types:
            Intensity_types[line["intensity"]] = 1
        else:
            Intensity_types[line["intensity"]] += 1
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
    for value in log:
        if(value["intensity"] == "high"):
            high_intensity.add(f"Day: {value['day']}, Workout Info: Type: {value['type']}, Time: {value['minutes']}, Intensity: {value['intensity']}")
        if(int(value["minutes"]) > 60):
            high_intensity.add(f"Day: {value['day']}, Workout Info: Type: {value['type']}, Time: {value['minutes']}, Intensity: {value['intensity']}")
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
            option_One("Set")
        else: 
            print(f"Current Info: Name: {user_exists['name']}, Level: {user_exists['goal']}")
            option_One("Update")
    elif choice == 2:
        option_Two()
    elif choice == 3:
        option_Three()
    elif choice == 4:
        option_Four()
    elif choice == 5:
        option_Five()
    elif choice == 6:
        log = []
        day = 0
        print("Reset Data Complete")
    elif choice == 7:
        with open("log.json", "w") as file:
            data = {

            }
            data["profile"] = user_exists
            data["logs"] = log
            json.dump(data, file, indent=4)
        break
print("Thank You For Visiting")
