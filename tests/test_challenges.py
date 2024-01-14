import unittest
import json
import os

from challenges import valleys, clouds, strings, markdown,queens, graphs, LessonModule

class TestChallenges(unittest.TestCase):
    def test_number_of_valleys(self):
        r = valleys.count(8,"UDDDUDUU")
        self.assertEqual(1,r)

    def test_number_of_cloud_jumps(self):
        c = [0, 0, 0, 0, 1, 0]
        r = clouds.jumps_count(c)
        self.assertEqual(3,r)

    def test_repeatedin_strings(self):
        s = 'aba'
        n = 10
        r = strings.repeatedIn(s, n)
        self.assertEqual(7, r)
        s = 'a'
        n = 1000000
        r = strings.repeatedIn(s, n)
        self.assertEqual(n, r)

    def test_grep(self):
        s = 'hello world hello'
        t = 'ello'
        r = strings.grep(s, t)
        self.assertEqual([1,13],r)

    def test_markdown(self):
        s = "1\n2\n\n~~3~~\nrob\n>foo\n>bar\n1";
        #r = markdown.process(s)
        #print(r)

    def test_queens_attack(self):
        r = queens.attack(5,3,4,3,[[5,5],[4,2],[2,3]])
        self.assertEqual(r,10)
        r = queens.attack(4,0,4,4, [])
        self.assertEqual(r,9)

    def test_all_paths1(self):
        # g = [[1,2], [3], [3], []]
        # e = [[0,1,3],[0,2,3]]
        # r = graphs.allpathsSourceToTarget1(g, [[0]], 3)
        # self.assertEqual(r,e)
        G = {'A':['B','C'], 'B':['D'], 'C':['D', 'F'], 'D':['E', 'F'], 'E':['F']}
        # g = [['B', 'C'], ['D'], ['D']]
        # e = [['A','B', 'D'], ['A','C','D']]
        # r = graphs.allpathsSourceToTarget1(g,[['A']], 'D')
        #r = graphs.ap2(G, 'A','F')
        #print('r',r)
        #r = graphs.all_paths(G, 'A', 'F')
        #print(r)

    def test_a_lesson(self):
        lesson_path = "/Users/rrogers/Downloads/takehome-backend-engineer/labels.json"
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
        self.assertEqual(len(routes), numberOfRoutes)
        prettyRoutes = lessons.prettyConversationRoutes()
        print(prettyRoutes)

    def test_a_another_lesson(self):
        lesson_path = "/Users/rrogers/Downloads/takehome-backend-engineer/allornothing.json"
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
        lesson_path = "/Users/rrogers/Downloads/takehome-backend-engineer/labels.json"
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




if __name__ == '__main__':
    unittest.main()
