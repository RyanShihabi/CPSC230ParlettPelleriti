'''
For the questions below, assume that student dictionaries have the following keys:
- Name ( their first and last name as a single string)
- GPA ( a float with their GPA)
- Major ( a string with their major)
- Classes_Taken (a list of all the course codes--e.g. CPSC 392--they’ve taken)
- Expected_Graduation (an int of the year they expect to graduate)
- Favorite_Class (a string of a course code--e.g. CPSC 392)
5. Write a function, tough_majors(), which takes in a list, fowler_students,
as an argument. The list, fowler_students, is a list of multiple student
dictionaries structured the same way as in #1. Assume there could be any number
of students in the list.
The majors for fowler students are: “computer science”, “electrical engineering”,
“computer engineering”, “data science”, and “software engineering”. Raise an
error if the major of one of the students is not one of those 5.
For each of these 5 majors, calculate the mean GPA for students in each major,
and return a dictionary with the mean GPAs for each major (e.g.
{“computer science” : 0, “electrical engineering”: 0, “computer engineering”: 0,
“data science”: 0,“software engineering”: 0}, but with the actual means instead
 of 0’s).
'''

def tough_majors(fowler_students):
    majors = ["computer science", "electrical engineering", "computer engineering", "data science", "software engineering"]

    for student in fowler_students:
        if student["Major"] not in majors:
            raise ValueError("student not in a fowler major")

    major_count = {}
    major_cumulative = {}
    major_mean_GPA = {}

    for student in fowler_students:
        major_count[student["Major"]] = major_count.get(student["Major"], 0) + 1
        major_cumulative[student["Major"]] = major_cumulative.get(student["Major"], 0) + student["GPA"]

    for major in major_count:
        major_mean_GPA[major] = major_cumulative[major]/major_count[major]

    return major_mean_GPA
