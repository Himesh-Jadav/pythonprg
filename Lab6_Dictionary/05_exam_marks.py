# Exam marks: +4 correct, -1 wrong
key = ("A", "B", "C")
students = {
    "Amit": ("A", "B", "C"),
    "Rahul": ("A", "C", "C")
}

marks = {}
for name, answers in students.items():
    marks[name] = sum(
        4 if answers[i] == key[i] else -1
        for i in range(len(key))
    )

print(marks)
