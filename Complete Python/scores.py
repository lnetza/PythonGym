student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for nombre,calificacion in student_scores.items():
    if calificacion <= 70:
        student_grades[nombre]="Fail"
    if calificacion >= 71 and calificacion <=80:
        student_grades[nombre]="Acceptable"
    if calificacion >= 81 and calificacion <=90:
        student_grades[nombre]="Exceeds Expectations"
    if calificacion >= 91:
        student_grades[nombre]="Outstanding"


print(student_grades)