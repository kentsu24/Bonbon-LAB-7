def calculate_final_grade():
  """Calculates and displays a student's final grade based on three period grades."""

  prelim_grade = float(input("Enter Preliminary Period Grade: "))
  midterm_grade = float(input("Enter Midterm Period Grade: "))
  final_grade = float(input("Enter Final Period Grade: "))

  # Validate input grades
  if not (40 <= prelim_grade <= 100 and 40 <= midterm_grade <= 100 and 40 <= final_grade <= 100):
    print("Error: Grade input must be between the range of 40 - 100.")
    return

  # Calculate grade points
  grade_points = round((prelim_grade * 0.3333) + (midterm_grade * 0.3333) + (final_grade * 0.3333), 2)

  # Determine grade description
  grade_description = ""
  if grade_points >= 99:
    grade_description = "Excellent"
  elif grade_points >= 96:
    grade_description = "Outstanding"
  elif grade_points >= 93:
    grade_description = "Superior"
  elif grade_points >= 90:
    grade_description = "Very Good"
  elif grade_points >= 87:
    grade_description = "Good"
  elif grade_points >= 84:
    grade_description = "Satisfactory"
  elif grade_points >= 81:
    grade_description = "Fairly Satisfactory"
  elif grade_points >= 78:
    grade_description = "Fair"
  elif grade_points >= 75:
    grade_description = "Passed"
  else:
    grade_description = "Failed"

  # Display results
  print("Final Grade Points:", grade_points)
  print("Grade Description:", grade_description)

# Run the program
calculate_final_grade()



          

    
    