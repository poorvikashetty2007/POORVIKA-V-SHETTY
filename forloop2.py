total_jacks = 100
completed = 0
while completed < total_jacks:
    completed += 10
    print("\nYou have completed", completed, "jumping jacks.")
    if completed >= total_jacks:
        print("Congratulations! You completed the workout!")
        break
    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()       
        if skip in ["yes", "y"]:
            print("You completed a total of", completed, "jumping jacks.")
            break
        else:
            print(total_jacks - completed, "jumping jacks remaining. Keep going!")
    elif tired in ["no", "n"]:
        print(total_jacks - completed, "jumping jacks remaining. Keep going!")
    else:
        print("Invalid input! Please enter yes/y or no/n.")
