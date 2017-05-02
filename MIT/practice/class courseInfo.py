class courseInfo(object):

    def __init__(self, courseName):
        self.courseName = courseName
        self.psetsDone = []
        self.grade = "No Grade"

    def setPset(self, pset, score):
        self.psetsDone.append((pset, score))

    def getPset(self, pset):
        for (p, score) in self.psetsDone:
            if p == pset:
                return score

    def setGrade(self, grade):
        if self.grade == "No Grade":
            self.grade = grade

    def getGrade(self):
        return self.grade



class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))

    def setGrade(self, grade, course="6.01x"):
        """
        grade: integer greater than or equal to 0 and less than or equal to 100
        course: string

        This method sets the grade in the courseInfo object named by `course`.

        If `course` was not part of the initialization, then no grade is set, and no
        error is thrown.

        The method does not return a value.
        """
        #   fill in code to set the grade
        for s in self.myCourses:
            if course == s.courseName:
                s.setGrade(grade)


    def getGrade(self, course="6.02x"):
        """
        course: string

        This method gets the grade in the the courseInfo object named by `course`.

        returns: the integer grade for `course`.
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the grade
        for s in self.myCourses:
            if course == s.courseName:
                return s.getGrade()
        if course not in self.myCourses:
                return -1



    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        #   fill in code to set the pset
        for s in self.myCourses:
            if course == s.courseName:
                for k, v in s.psetsDone:
                    if pset == k:
                        s.psetsDone.pop(s.psetsDone.index((k,v)))
                s.setPset(pset,score)



    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        course: string

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the pset
        for s in self.myCourses:
            if course == s.courseName:
                if s.getPset(pset) == None:
                    return -1
                return s.getPset(pset)
            return -1


edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setPset(1,100)
print edX.getPset(1)# >>>100

edX.setPset(2,100,"6.00x")
print edX.getPset(2)# >>>100

edX.setPset(2,90,"6.00x")
edX.setPset(3,99,"6.02x")
print edX.getPset(3,'6.02')# >>>-1
print edX.getPset(2.1)# >>>-1

edX.setGrade(100)
print edX.getGrade("6.01x")# >>>100
for c in ["6.00x","6.01x","6.02x"]:
    edX.setGrade(90,c)
    print edX.getGrade(c)
    # >>>90
    # >>>100
    # >>>90


'''
The instance edX has several methods defined. The expression dir(edX) will evaluate to be all the methods defined in the class.

In this case dir(edX) will evaluate to the list:

>>> dir(edX)
["__init__", "setGrade","getGrade","setPset","getPset"]

-----The expression dir(edX)[2](90) is the same as edX.setGrade(90) ----------> False
'''