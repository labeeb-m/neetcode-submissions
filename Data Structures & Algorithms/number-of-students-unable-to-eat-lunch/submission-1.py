class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = collections.deque(students)
        sandwiches = collections.deque(sandwiches)

        
        while students and sandwiches[0] in students:
            if sandwiches[0] == students[0]:
                sandwiches.popleft()
                students.popleft()
            else:
                student = students[0]
                students.popleft()
                students.append(student)

        return len(students) if students else 0
