n_scores = []
for i in range(10):
    score = float(input(f"Please grade the student {i + 1} enter "))
    n_scores.append(score)

# تهیه کپی از لیست نمرات و مرتب‌سازی آن به صورت نزولی
sorted_scores = sorted(n_scores.copy(), reverse=True)

# پرسش از کاربر برای حذف نمره
remove_score = input("Do you want to delete a score? (Yes/No): ").strip().lower()
if remove_score == 'yes':
    score_to_remove = float(input("Please enter the grade you want to remove: "))
    if score_to_remove in sorted_scores:
        sorted_scores.remove(score_to_remove)
    else:
        print("The desired score does not exist in the list.")

# نمایش نمرات
print("Scores after elimination (if applicable):", sorted_scores)

# شمارش نمرات ۲۰
count_20 = sorted_scores.count(20)
print(f"The number of marks is 20: {count_20}")

# دریافت نمرات کلاس دوم
second_class_scores = []
for i in range(10):
    score = float(input(f"Please grade the student{i + 1} Enter the second class: "))
    second_class_scores.append(score)

# ترکیب نمرات کلاس اول و دوم
combined_scores = sorted_scores + second_class_scores
print("First and second grade combined grades:", combined_scores)

# پاک کردن کل عناصر موجود در لیست اول و دوم
sorted_scores.clear()
second_class_scores.clear()
print("The first and second list were deleted.")

# نمایش لیست سوم (ترکیبی)
print("The third list (combined):", combined_scores)


