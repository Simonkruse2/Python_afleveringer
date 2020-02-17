from mypackage.classes.course import Course

class DataSheet():
    def __init__(self, courses):
        self.courses = []
        for course in courses:
            new_course = Course(course.name, course.classroom, course.teacher, course.ETCS, course.grade)
            self.courses.append(new_course)
    
    def __repr__(self):
        return 'DataSheet(%r)' % (self.courses)

    # def __str__(self):
    #     return 'Courses:{courses}'.format(
    #         courses=self.courses)
    
    def get_grades_as_list(self):
        lst_grade = []
        for course in self.courses:
            lst_grade.append(course.grade)
        return lst_grade


if __name__ == "__main__":
    print("hello in datasheet")