import pandas as pd

student_data = pd.read_csv("Student_scores.csv")
print(student_data)

print(student_data.head(5))

print(student_data.columns.to_list())

print(student_data.shape)

print(student_data.isnull().sum())

numeric_columns = ['Maths', 'English', 'Physics', 'Chemistry', 'Biology']
student_data[numeric_columns] = student_data[numeric_columns].apply(lambda x: x.fillna(x.mean()))

print(student_data) 

student_data.to_csv("students_scores_clean.csv", index=False)

print(student_data)


student_data = pd.read_csv("students_scores_clean.csv")


print(student_data.describe())

descibe_data = student_data.describe()
descibe_data.to_csv("summary_data.csv",index=False)
print(descibe_data)

#  mean: The average score of all students for that subject.
#  std: Standard deviation — it shows how much the scores vary from the average.
#  25%: The score below which 25% of the students scored (1st quartile).
#  50%: The median — half the students scored below this value.
#  75%: The score below which 75% of the students scored (3rd quartile).


subjects = ['Maths', 'English', 'Physics', 'Chemistry', 'Biology']
print("Mean and Standard Deviation per subject:\n")
for subject in subjects:
    mean_score = student_data[subject].mean()
    std_score = student_data[subject].std()
    print(f"{subject}: Mean = {mean_score:.2f}, Std Dev = {std_score:.2f}")

student_data['Total'] = student_data[subjects].sum(axis=1)
student_data['Average'] = student_data['Total'] / len(subjects)
print("\nStudents with Average score above 70:\n")
print(student_data[student_data['Average'] > 70])

student_data_sorted = student_data.sort_values(by='Average', ascending=False)
# print("\nDataset sorted by Average (highest to lowest):\n")
print(student_data_sorted)



highest = student_data.loc[student_data['Total'].idxmax()]
lowest = student_data.loc[student_data['Total'].idxmin()]


print("\nStudent with the Highest Total:\n", highest)
print("\nStudent with the Lowest Total:\n", lowest)

student_data_sorted.to_csv("students_scores_with_totals.csv", index=False)
print("\n Updated dataset saved as 'students_scores_with_totals.csv'")

