prelim_grade = float(input("Enter Prelimanary Period Grade:"))
midterm_grade = float(input("Enter Midterm Period Grade:"))
final_grade = float(input("Enter Final Period Grade:"))

if (prelim_grade < 40 or prelim_grade > 100 or midterm_grade < 40 or midterm_grade > 100 or final_grade < 40 or final_grade > 100):
    print("Error: Grade input must be between the range of 40-100.")
else:
    grade_points = round((prelim_grade * 0.3333) + (midterm_grade * 0.3333) + (final_grade * 0.3333))
    print("Final Grade Points:", grade_points)
    print("Grade Description:" + str(grade_points))

    if grade_points >= 90 and grade_points <= 100:
        print("Excellent")
    elif grade_points >= 80 and grade_points <= 89:
        print("Very Good")
    elif grade_points >= 70 and grade_points <= 79:
        print("Good")
    elif grade_points >= 60 and grade_points <= 69:
        print("Satisfactory")
    elif grade_points >= 50 and grade_points <= 59:
        print("Fair")
    else:
        print("Failed")

        



          

    
    