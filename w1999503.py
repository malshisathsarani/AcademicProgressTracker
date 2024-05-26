total_progress = total_module_trailer = total_exclude = total_not_progress = 0


def logo():
    print()
    print(" _____                                     _____              _ _      _             ")
    print("|  __ \                                   |  __ \            | (_)    | |            ")
    print("| |__) | __ ___   __ _ _ __ ___  ___ ___  | |__) | __ ___  __| |_  ___| |_ ___  _ __ ")
    print("|  ___/ '__/ _ \ / _` | '__/ _ \/ __/ __| |  ___/ '__/ _ \/ _` | |/ __| __/ _ \| '__|")
    print("| |   | | | (_) | (_| | | |  __/\__ \__ \ | |   | | |  __/ (_| | | (__| || (_) | |   ")
    print("|_|   |_|  \___/ \__, |_|  \___||___/___/ |_|   |_|  \___|\__,_|_|\___|\__\___/|_|   ")
    print("                  __/ |                                                              ")
    print("                 |___/ ")
    print("_____________________________________________________________________20221150:Kavindu\n")


def student_progress_display_function(student_progress_display):
    """Taking student data list and add it to the txt file."""
    print("\n----> Print data in the txt file <-----\n")
    for small_progress_lists in student_progress_display:  # Taking nested lists one at a time.
        progress_name = small_progress_lists[-1]  # Taking last element in the list and set in to a variable.
        small_progress_lists.pop(-1)
        txt_data = f"{progress_name} : {small_progress_lists}\n"

        with open("progress_contain.txt", "a") as file:  # Adding data to txt file
            file.write(txt_data)

    file = open("progress_contain.txt")  # Open data file and print line by line
    lines = file.readlines()
    for line in lines:
        print(line)


def histogram(total_progress, total_module_trailer, total_not_progress, total_exclude):
    print("-----------------------------------------------------------------------")
    print("*** Histogram ***\n")
    print(f"Progress {total_progress}  : ", total_progress * "*")
    print(f"Trailer {total_module_trailer}   : ", total_module_trailer * "*")
    print(f"Retriever {total_not_progress} : ", total_not_progress * "*")
    print(f"Excluded {total_exclude}  : ", total_exclude * "*")
    print()
    print(f"{total_progress + total_module_trailer + total_not_progress + total_exclude} outcomes in total.")
    print("-----------------------------------------------------------------------")


def progression_outcome(credits_at_pass, defer, fail):
    """Taking user inputs and return Progression outcome"""
    global total_progress, total_module_trailer, total_exclude, total_not_progress
    if credits_at_pass == 120 and defer == 0 and fail == 0:
        total_progress += 1
        return "*** Progress ***"
    elif credits_at_pass == 100 and 20 in [defer, fail]:
        total_module_trailer += 1
        return "*** Progress(module trailer) ***"
    elif credits_at_pass in [0, 20, 40] and fail in [80, 100, 120]:
        total_exclude += 1
        return "*** Exclude ***"
    else:
        total_not_progress += 1
        return "*** Do not progress - module retriever ***"


def data_input_function(should_continue, marks, student_or_staff):
    """This function take student inputs and make calculate outcome"""
    student_progress_display, student_data_dic = [], {}
    while should_continue:
        student_data_list = []
        try:
            student_id = input("Please enter your student ID: ").lower()
            if len(student_id) != 8 or student_id[0] != "w":
                print("Invalid student ID. ex: w1234567 (must start with w and 7 digits).\n")
                continue
            credits_at_pass = int(input("Please enter your credits at pass: "))
            if credits_at_pass not in marks:
                print("Out of range.\n")
                continue
            defer = int(input("Please enter your credits at defer: "))
            if defer not in marks:
                print("Out of range.\n")
                continue
            fail = int(input("Please enter your credits at fail: "))
            if fail not in marks:
                print("Out of range.\n")
                continue
        except ValueError:
            print("Integer required.\n")
            continue

        if (credits_at_pass + defer + fail) != 120:  # Check validation of total marks
            print("Total incorrect.\n")
            continue

        if student_or_staff == 1:
            print(progression_outcome(credits_at_pass, defer, fail))
            break

        else:
            student_data_list += credits_at_pass, defer, fail  # Adding marks to a list
            student_progress = progression_outcome(credits_at_pass, defer, fail)  # call progress outcome function
            print(student_progress)
            student_data_list.append(student_progress)  # Appending progress to a list
            student_data_dic[student_id] = student_data_list  # Add ID as key and marks as value to a dictionary
            student_progress_display.append(student_data_list)  # Add data list to another list
            print()
            run_again = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
            print()
            if run_again != "y":
                should_continue = False
                histogram(total_progress, total_module_trailer, total_not_progress, total_exclude)  # histogram function
                for key, value in student_data_dic.items():  # Print data in the dictionary
                    print(key, ":", value)
                print("-----------------------------------------------------------------------")
                student_progress_display_function(student_progress_display)
                print()


def main():
    """main function is to act as the starting point of execution for program"""
    marks = (0, 20, 40, 60, 80, 100, 120)  # Define possible marks.
    logo()
    student_or_staff = int(input("Please enter 1 for student version or 2 for staff version: "))  # Check version
    print()
    if student_or_staff == 1:
        should_continue = 1
        data_input_function(should_continue, marks, student_or_staff)
    else:
        should_continue = True
        data_input_function(should_continue, marks, student_or_staff)


main()
        






