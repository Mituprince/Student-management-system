import json  #module importing for student management system

MITHUN_PROJECT = "mithun.json"  #name of the project

# Function to load student records from a JSON file
def pack_candidates():
    try:
        with open(MITHUN_PROJECT, 'r') as file:
            candidates = json.load(file)
    except FileNotFoundError:
        candidates = []
    return candidates

# Function to save student records to a JSON file
def save_candidates(candidates):
    with open(MITHUN_PROJECT, 'w') as file:
        json.dump(candidates, file, indent=4)

# Function to add a new student record
def add_candidate():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = input("Enter student's grade: ")
    mail= input("Enter student's email details: ")

    candidates = pack_candidates()
    candidates.append({"name": name, "age": age, "grade": grade, "email": mail})
    save_candidates(candidates)
    print("candidate record added successfully!")

# Function to view all existing student records
def view_candidates():
    candidates = pack_candidates()
    if candidates:
        print("\nCandidate Records:")
        for candidate in candidates:
            print(f"Name: {candidate['name']}, Age: {candidate['age']}, Grade: {candidate['grade']}, mail: {candidate['email']}")
    else:
        print("No student records found.")

# Function to search for a specific student by name or grade
def find_candidate():
    quest = input("Enter the name or grade of the candidate to search: ")

    candidates = pack_candidates()
    found_candidates = []
    for candidate in candidates:
        if quest.lower() in candidate['name'].lower() or quest.lower() == candidate['grade'].lower():
            found_candidates.append(candidate)

    if found_candidates:
        print("\nFound Candidates:")
        for candidate in found_candidates:
            print(f"Name: {candidate['name']}, Age: {candidate['age']}, Grade: {candidate['grade']}, mail: {candidate['email']}")
    else:
        print("No matching candidate records found.")

# Function to modify a student's information
def modify_candidate():
    quest = input("Enter the name of the candidate to modify: ")

    candidates = pack_candidates()
    for candidate in candidates:
        if quest.lower() in candidate['name'].lower():
            print(f"Candidate Found: Name: {candidate['name']}, Age: {candidate['age']}, Grade: {candidate['grade']}, Mail: {candidate['email']}")
            new_age = int(input("Enter modified age: "))
            new_grade = input("Enter modified grade: ")
            new_mail = input("Enter modified mail details: ")
            candidate['age'] = new_age
            candidate['grade'] = new_grade
            candidate['email'] = new_mail
            save_candidates(candidates)
            print("Candidate record modified successfully!")
            return
    print("No matching candidate found.")

# Function to erase a student record
def erase_candidate():
    quest = input("Enter the name of the candidate to erase: ")

    candidates = pack_candidates()
    modified_candidates = [candidate for candidate in candidates if quest.lower() not in candidate['name'].lower()]

    if len(modified_candidates) < len(candidates):
        save_candidates(modified_candidates)
        print("Candidate record erased successfully!")
    else:
        print("No matching candidate found.")

# Main function to provide a simple command-line interface
def main_function():
    while True:
        print("\nStudent Management System")
        print("1. Add Candidate")
        print("2. View Candidate")
        print("3. Find Candidate")
        print("4. Modify Candidate")
        print("5. Erase Candidate")
        print("0. Exit")

        pick = input("Enter your pick: ")

        if pick == '1':
            add_candidate()
        elif pick == '2':
            view_candidates()
        elif pick == '3':
            find_candidate()
        elif pick == '4':
            modify_candidate()
        elif pick == '5':
            erase_candidate()
        elif pick == '0':
            break
        else:
            print("Invalid pick. Please try again.")

if __name__ == "__main__":
    main_function()