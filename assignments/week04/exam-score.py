scores = []

for i in range(5):
    score = int(input("Enter score of student " + str(i + 1) + ": "))
    scores.append(score)

print()

for i in range(5):
    if scores[i] >= 50:
        result = "ผ่าน"
    else:
        result = "ไม่ผ่าน"

    print("Student", i + 1, ":", scores[i], "=>", result)