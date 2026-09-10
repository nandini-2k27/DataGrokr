def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def get_valid_subject_count():
    while True:
        try:
            count = int(input("Enter number of subjects: "))

            if count > 0:
                return count
            else:
                print("Number of subjects must be greater than 0.")

        except ValueError:
            print("Please enter a valid whole number.")


def calculate_student_result():
    print("=" * 40)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 40)

    student_name = input("Enter student name: ").strip()

    while not student_name:
        print("Student name cannot be empty.")
        student_name = input("Enter student name: ").strip()

    num_subjects = get_valid_subject_count()

    subjects = {}

    print("\nEnter subject details")
    print("-" * 40)

    for i in range(num_subjects):
        while True:
            subject = input(f"Enter subject {i + 1} name: ").strip()

            if subject:
                break
            else:
                print("Subject name cannot be empty.")

        marks = get_valid_marks(subject)
        subjects[subject] = marks

    total_marks = sum(subjects.values())
    average = total_marks / num_subjects

    grade = calculate_grade(average)

    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print("\n" + "=" * 40)
    print("              RESULT")
    print("=" * 40)

    print(f"Student Name : {student_name}")
    print(f"Total Marks  : {total_marks:.2f}")
    print(f"Average      : {average:.2f}%")
    print(f"Grade        : {grade}")
    print(f"Result       : {result}")

    print("\nSubject-wise Marks")
    print("-" * 40)

    for subject, marks in subjects.items():
        print(f"{subject:<20} : {marks:.2f}")

    print("=" * 40)


if __name__ == "__main__":
    calculate_student_result()