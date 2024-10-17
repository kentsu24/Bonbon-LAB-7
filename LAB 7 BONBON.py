prelim_grade = float(input("Enter Prelimanary Period Grade:"))
midterm_grade = float(input("Enter Midterm Period Grade:"))
final_grade = float (input("Enter Final Period Grade:"))
        
if ( prelim_grade >=40 and prelim_grade <= 100 and midterm_grade >=40 and midterm_grade <= 100 and  final_grade >=40 and final_grade<= 100):
        print ("Error: Grade input must between the range of 40-100.")
            
grade_points = round((prelim_grade * 0.3333) + (midterm_grade * 0.3333) + (final_grade * 0.3333))
print("nFinal Grade Points:",grade_points)
print("Grade Desription:" + str (grade_points))

if grade_points >= 99 and grade_points <= 100:
        print ("Excellent")
elif grade_points ==1.25:
        print ("Outstanding")
elif grade_points == 1.50:
        print ("Superior")
elif grade_points == 1.75:
        print ("Very Good")
elif grade_points == 2.00:
        print ("Good")
elif grade_points == 2.25:
        print ("Satisfactory")
elif grade_points == 2.50:
        print ("Fairly Satisfactory")
elif grade_points == 2.75:
        print ("Fair")
elif grade_points == 3.00:
        print ("Passed")
else:
        print ("Failed")
        
grade_points >= 100 and <= 98
        



          

    
    