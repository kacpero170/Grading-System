# Students in class
lloyd = {"name": "Lloyd", "homework": [90.0, 97.0, 75.0, 92.0], "quizzes": [88.0, 40.0, 94.0], "tests": [75.0, 90.0]}
alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0], "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0]}
tyler = {"name": "Tyler", "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0], "tests": [100.0, 100.0]}
ryan = {"name": "Ryan", "homework": [80.0, 72.0, 60.0, 10.0], "quizzes": [60.0, 30.0, 64.0], "tests": [76.0, 65.0]}
bill = {"name": "Bill", "homework": [20.0, 50.0, 90.0, 44.0], "quizzes": [50.0, 48.0, 88.0], "tests": [90.0, 78.0]}
students = [lloyd, alice, tyler, ryan, bill]

# Average definition
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

# Gettting the average numerical grade
homework_weight = 0.1
quizzes_weight = 0.3
tests_weight = 0.6

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return (homework_weight * homework) + (quizzes_weight * quizzes) + (tests_weight * tests)

# Getting the letter grade
def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

# Getting the class average
def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

# Results
def print_all_grades(students):
  for student in students:
    student_name = student["name"]
    student_avg = get_average(student)
    letter_grade = get_letter_grade(student_avg)
    print(f"{student_name} got an average numerical grade of {student_avg:.2f} and a {letter_grade} letter grade.")
print_all_grades(students)
print("The class got an average numerical grade of "+str(round(get_class_average(students), 2))+" and a "+str(get_letter_grade(get_class_average(students)))+" letter grade.")