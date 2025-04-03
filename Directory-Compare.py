import os
import json

BASEDIR = "C:\\msys64\\"

def recursive_get(base_dir):
    dictionary = {}
    for x in os.listdir(base_dir):
        if os.path.isdir(base_dir + x):
            dictionary[x] = recursive_get(base_dir + x + "\\")
        elif os.path.isfile(base_dir + x):
            dictionary[x] = os.path.getsize(base_dir + x)
    return dictionary

def recursive_compare(comp1, comp2, base_dir):
    error_string = ""
    print(base_dir)
    for x in comp1:
        if os.path.isdir(base_dir + x):
            if x in comp2:
                error_string += recursive_compare(comp1[x], comp2[x], base_dir + x + "\\")
            else:
                error_string += "\nfolder " + base_dir + x + " not in instance 2"
        elif os.path.isfile(base_dir + x):
            if x not in comp2:
                error_string += "\nfile " + base_dir + x + " not in instance 2"
            elif comp1[x][1] != comp2[x][1]:
                error_string += "\nfile " + base_dir + x + " is different: inst1-" + str(comp1[x]) + " inst2-" + str(comp2[x])
    for x in comp2:
        if os.path.isdir(base_dir + x):
            if x in comp1:
                error_string += recursive_compare(comp1[x], comp2[x], base_dir + x + "\\")
            else:
                error_string += "\nfolder " + base_dir + x + " not in instance 1"
        elif os.path.isfile(base_dir + x):
            if x not in comp2:
                error_string += "\nfile " + base_dir + x + " not in instance 2"
    return error_string

def continue_use():
    user_input = "z"
    while user_input.lower() != "y" and user_input.lower() != "n":
        print("Would you like to continue?")
        user_input = input(" (y/n) >> ")
    return user_input.lower() == "y"

def get_option():
    user_input = "z"
    while user_input.lower() not in ["a", "b", "c", "d"]:
        print("What would you like to do?")
        print(" A) Get an instance")
        print(" B) Compare instances")
        print(" C) Save instance 1")
        print(" D) Save instance 2")
        user_input = input(" >> ")
    return user_input.lower()

if __name__ == "__main__":
    dict1 = {}
    dict2 = {}
    print("")
    print("Hello World!")
    print("------------")
    print("")
    print("This is a test to see what happens in the gcc compiler.")
    print("")
    while continue_use():
        user_option = get_option()
        if user_option == 'a':
            # get instance
            print("Getting a new instance...")
            dict2 = dict1
            print(" Overwrote instance 2 with instance 1")
            dict1 = recursive_get(BASEDIR)
            print(" Retrieved instance 1")
        elif user_option == 'b':
            # compare instance
            print(recursive_compare(dict1, dict2, BASEDIR))
        elif user_option == 'c':
            # instance 1
            print("Saving instance 1")
            json.dump(dict1, open("instance1.json", 'w'), indent = 1)
        elif user_option == 'd':
            # instance 2
            print("Saving instance 2")
            json.dump(dict2, open("instance2.json", 'w'), indent = 1)
    print("Good-bye")
