from collections import deque
class Lesson:
    def __init__(self, lessonDict):
        for k,v in lessonDict.items():
            setattr(self,k,v)
    def neighbors(self):
        return self.routes.split("|")

class Lessons:
    def __init__(self, lessonSet):
        self.lessons = {}
        for lessonData in lessonSet.values():
            self.lessons.append(Lesson(lessonData))

        self.start = []
        self.ends = []

        for lesson in self.lessons:
            if lesson.tag == 'labels-start':
                self.starts.append(lesson)
            if lesson.tag == 'bye':
                self.ends.append(lesson)

        if not len(self.starts):
            raise Exception("We really need an startpoint. Please provide one with the proper tag")

        if len(starts) > 1:
            raise Exception("A Lesson has only one starting place, you have: " + len(starts))

        if not len(self.ends):
            raise Exception("This lesson should have an ending please provide one. Bye!")



    def startTag(self):
        return self.start.tag

    def endTags(self):
        return [lesson.id in self.ends]

