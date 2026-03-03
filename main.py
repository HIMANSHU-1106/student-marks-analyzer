#numpy importing
import numpy as np
#storing data
headerrow = np.array(["Roll no.", "DM", "OS", "SE", "AI", "DBMS"])
marksdata = np.array([[1, 78, 65, 82, 74, 69], [2, 56, 72, 61, 88, 79], [3, 91, 84, 76, 69, 73], [4, 64, 58, 71, 62, 55], [5, 88, 92, 85, 90, 87], [6, 47, 53, 60, 49, 58], [7, 69, 75, 80, 72, 77], [8, 95, 89, 94, 91, 90], [9, 52, 48, 57, 63, 59], [10, 83, 78, 74, 86, 81]])
#function for average marks of each subject
def average_of_subject():
    for a in range (1, marksdata.shape[1]  ) :
        subavg = np.mean(marksdata[: , a])
        print(f"The average of subject{headerrow[a]} marks is {subavg}.")


#function for highest marks roll no in each subject
def highest_score_in_subject():
    for b in range(1, marksdata.shape[1] ) :
        maxsub = np.max(marksdata[: , b])
        subcolumn = marksdata[1: , b]
        submaxindex = np.argmax(subcolumn)
        rollnomaxsub = marksdata[submaxindex + 1, 0]
        print(f"Max marks in {headerrow[b]} are {maxsub} by student roll no {rollnomaxsub}")

    #function for average marks student wise
def average_of_student():
    for c in range(0, marksdata.shape[0]) :
        studentavg = np.mean(marksdata[ c, 1:])
        print(f"The average marks scored by student roll no {marksdata[c , 0]} are {studentavg}")
#function for ranks of students
def rank_students():
    totals = np.sum(marksdata[ : , 1: ], axis=1)
    ranksasc = np.argsort(totals)
    ranks = np.flip(ranksasc)
    print(f"The ranks of the students acc to roll no are {marksdata[ranks, 0]}")
    
   
#finding top d students
def top_students(d) :
    totalmarksst = np.sum(marksdata[: , 1:], axis=1)

    rankedasc = np.argsort(totalmarksst)

    final_list = np.flip(rankedasc)


    print(f"The top {d} students' rollno are {marksdata[final_list[0:d], 0]}.")
    #finding failed students
def failed_students():
    # Extract only subject marks (ignore roll column)
    subject_marks = marksdata[:, 1:]
    
    # Boolean mask where marks < 50
    fail_mask = subject_marks < 50
    
    # Check row-wise if any subject is failed
    failed_indices = np.where(np.any(fail_mask, axis=1))[0]
    
    if len(failed_indices) == 0:
        print("No student has failed.")
        return
    
    for e in failed_indices:
        roll_no = marksdata[e, 0]
        failed_subjects = headerrow[1:][fail_mask[e]]
        
        print(f"Roll no {roll_no} failed in subjects: {', '.join(failed_subjects)}")


#calling functions
average_of_subject()
highest_score_in_subject()
average_of_student()
rank_students()
top_students(5)
failed_students()