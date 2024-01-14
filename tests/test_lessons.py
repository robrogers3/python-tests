import unittest
import json
import os

from src import LessonModule

class TestLessons(unittest.TestCase):
    def test_a_lesson(self):
        lesson_path = "labels.json"
        lessons = None
        with open(lesson_path) as json_file:
            data = json.load(json_file)
            lessons = LessonModule.Lessons(data, 'labels')

        self.assertEqual(lessons.startTag(), 'LUU')
        self.assertEqual(lessons.endTags(), ['ANG'])

        lesson = lessons.findById('GYU')
        self.assertEqual(True, lesson.isEndingPoint())
        self.assertEqual(True, lessons.reachedEndingPoint('GYU'))
        self.assertEqual(True, lessons.reachedEndingPoint('ANG'))

        routes = lessons.conversationRoutes()
        numberOfRoutes = lessons.numberOfConversationRoutes()
        self.assertEqual(4, numberOfRoutes)

    def test_a_another_lesson(self):
        lesson_path = "allornothing.json"
        lessons = None
        with open(lesson_path) as json_file:
            data = json.load(json_file)
            lessons = LessonModule.Lessons(data, os.path.basename(lesson_path).split('.')[0])

        self.assertEqual(lessons.startTag(), 'EIC')
        self.assertEqual(lessons.endTags(), ['YMB','OWQ'])
        self.assertEqual(lessons.starts[0].id, 'EIC')
        routes = lessons.conversationRoutes()
        numberOfRoutes = lessons.numberOfConversationRoutes()
        self.assertEqual(6, numberOfRoutes)
        prettyRoutes = lessons.prettyConversationRoutes()


    def test_lesson_loader(self):
        lesson_path = "labels.json"
        lessons = LessonModule.LessonLoader().load(lesson_path)
        self.assertEqual(lessons.startTag(), 'LUU')
        self.assertEqual(lessons.endTags(), ['ANG'])

        lesson = lessons.findById('GYU')
        self.assertEqual(True, lesson.isEndingPoint())
        self.assertEqual(True, lessons.reachedEndingPoint('GYU'))
        self.assertEqual(True, lessons.reachedEndingPoint('ANG'))

        routes = lessons.conversationRoutes()
        numberOfRoutes = lessons.numberOfConversationRoutes()
        self.assertEqual(4, numberOfRoutes)

    def test_we_get_an_error_for_404(self):
        lesson_path = "404.json"
        with self.assertRaises(FileNotFoundError):
            lessons = LessonModule.LessonLoader().load(lesson_path)

if __name__ == '__main__':
    unittest.main()
