from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    name = 'Test'
    courses = {'math': ['hard']}

    def setUp(self):
        self.student = Student('Test', {'math': ['hard']})

    def test_init(self):
        self.assertEqual('Test', self.student.name)
        self.assertEqual(self.courses, self.student.courses)

    def test_courses_empty(self):
        student = Student(self.name)
        self.assertTrue(isinstance(student.courses, dict))

    def test_enroll_when_course_exists_add_notes(self):
        result = self.student.enroll('math', ['test_note'])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        courses_result = {'math': ['hard', 'test_note']}
        self.assertEqual(courses_result, self.student.courses)

    def test_enroll_when_adding_new_course_in_courses(self):
        result = self.student.enroll('english', ['test_note'], 'Y')
        self.assertEqual(result, "Course and course notes have been added.")
        courses_result = {'math': ['hard'], 'english': ['test_note']}
        self.assertEqual(courses_result, self.student.courses)
        result2 = self.student.enroll('test', ['test_note'])
        self.assertEqual(result2, "Course and course notes have been added.")

    def test_enroll_when_adding_a_new_course_without_notes(self):
        result = self.student.enroll('english', ['test_note'], 'N')
        self.assertEqual(result, "Course has been added.")
        courses_result = {'math': ['hard'], 'english': []}
        self.assertEqual(courses_result, self.student.courses)

    def test_add_notes_when_course_exists_append_notes(self):
        result = self.student.add_notes('math', ['test'])
        courses_result = {'math': ['hard', ['test']]}
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(courses_result, self.student.courses)

    def test_add_notes_when_course_does_not_exist_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('test', ['test'])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_when_course_exists(self):
        result = self.student.leave_course('math')
        self.assertEqual(result, "Course has been removed")
        self.assertEqual({}, self.student.courses)

    def test_leave_course_when_course_does_not_exist_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('test')
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")


if __name__ == '__main__':
    main()
