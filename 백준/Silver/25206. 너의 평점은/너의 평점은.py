import sys
input = sys.stdin.readline

G = {'A+':4.5, 'A0':4.0 ,
     'B+':3.5, 'B0':3.0,
    'C+':2.5, 'C0':2.0,
    'D+':1.5, 'D0':1.0,
    'F':0,}

subjects = []
scores = []
grades = []

total_score = 0
total_grade = 0

for i in range(20):
    subject, score, grade = input().split()
    subjects.append(subject)
    scores.append(float(score))
    grades.append(grade)

for i in range(20):
    if grades[i] != 'P':
        total_score += scores[i]
        total_grade += scores[i] * G[grades[i]]


avg = total_grade / total_score
print(avg)

 