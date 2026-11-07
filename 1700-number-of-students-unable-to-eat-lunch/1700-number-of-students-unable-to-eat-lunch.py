class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        c=0
        while True:
            c = 0
            if len(students) == 0:
                return 0
            for i in range(len(students)):
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                    c=0
                else:
                    students.append(students.pop(0))
                    c=c+1
                if c == len(students):
                    return(len(students))