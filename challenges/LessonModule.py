from collections import deque
import json
import os
import sys
import getopt

class LessonLoader:
    """
    LessonLoader:
    I just use json to load a lessons file,
    and then populate Lessons from the json data.
    """
    def load(self, path_to_json_file):
        data = dict()
        with open(path_to_json_file) as json_file:
            data = json.load(json_file)
        return Lessons(data, os.path.basename(path_to_json_file).split(".")[0])

class Lesson:
    """
    Lesson:
    I am a Lesson, and have important attributes like:
    - neighbors: I've got next conversation routes
    - isEndingPoint: I know if I'm an ending point in a Lesson set
    """

    def __init__(self, lessonDict):
        for k,v in lessonDict.items():
            setattr(self,k,v)

    def __str__(self):
        return f"{self.id} -> [{self.routes}]"

    def __repr__(self):
        return f"{self.id}"

    def neighbors(self):
        return self.routes.split("|")

    def isEndingPoint(self):
        return getattr(self, 'tag', '') == 'bye' or getattr(self, 'stage', '') == 'endpoint'


class Lessons:
    """
    Lessons:
    I'm a container for a Lesson set, and I store the individual Lessons in a dictionary
    I can do a couple things, like:
    - Tell you if you reached an satisfactory end point, or
    - Tell you all the ways to reach the end of a conversation

    But know that, I need a single start lesson, and at least one end lesson!
    """
    def __init__(self, lessonSet, lessonName):
        self.lessons = {}
        self.name = lessonName
        for lessonData in lessonSet.values():
            lesson = Lesson(lessonData)
            self.lessons[lesson.id] = lesson

        self.starts = []
        self.ends = []
        startTagName = lessonName.lower() + '-start'
        for lesson in self.lessons.values():
            if lesson.tag == startTagName:
                self.starts.append(lesson)
            if lesson.tag == 'bye':
                self.ends.append(lesson)

        if not len(self.starts):
            raise Exception("A Lesson set requires a startpoint. Please provide one with the proper tag")

        if len(self.starts) > 1:
            raise Exception("A Lesson set should only have one starting place, you have: " + len(starts))

        if not len(self.ends):
            raise Exception("This Lesson set requires an ending. Please provide one with the proper tag.")

    def startTag(self):
        return self.starts[0].id

    def endTags(self):
        return [lesson.id for lesson in self.ends]

    def findById(self, id):
        lesson =  self.lessons.get(id, None)
        if not lesson:
            raise Exception("No lesson with id {id} found")
        return lesson

    def reachedEndingPoint(self,id):
        lesson = self.findById(id)
        return lesson.isEndingPoint()

    def conversationRoutes(self):
        result = []
        q = deque([[self.starts[0]]])
        endTags = set(self.endTags())

        while q:
            path = q.popleft()
            currentLesson = self.lessons[path[-1].id]
            neighbors = currentLesson.neighbors()
            for id in neighbors:
                if id in [lesson.id for lesson in path]:
                    # cycle found in path, discard
                    continue;

                if id not in self.lessons:
                    raise Exception("The conversation has no end")

                lesson = self.lessons[id]

                # path reaches end of lesson
                if lesson.id in endTags:
                    result.append(path + [lesson])
                else:
                    q.append(path + [lesson])

        return result

    def prettyConversationRoutes(self):
        routes = []
        for route in self.conversationRoutes():
            routes.append('->'.join([lesson.id for lesson in route]))

        return "[" + "], [".join(routes) + "]"

    def numberOfConversationRoutes(self):
        return len(self.conversationRoutes())


def usage():
    usage = """
Usage:
    -h prints this message
    -f the path to the lesson file in json format (required)
    -k key used to determine if a user has reached an end stage in a conversation, or
    -p show all conversation paths (aka. routes)
    """
    print(f"{os.path.basename(sys.argv[0])} [-h| -f path/to/lesson_file.json -p|-k ID]")
    print(usage)
    sys.exit(0)

if __name__ == '__main__':
    lesson_path = None
    key = None
    showPaths = False
    showUsage = False
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hpk:f:")
        for opt, arg in opts:
            if opt == "-h":
                showUsage = True

            if opt == "-f":
                lesson_path = arg

            if opt == "-k":
                key = arg

            if opt == "-p":
                showPaths = True
    except:
        usage()

    if showUsage:
        usage()

    if not lesson_path:
        print("\nPlease provide a path to the lesson file\n")
        usage()

    lessons = LessonLoader().load(lesson_path)

    if key:
        if lessons.reachedEndingPoint(key):
            print(f"You worked up to the lesson on {key} which is a decent pause in our conversation.")
        else:
            print(f"You have just got up to the lesson on {key}, consider picking up our conversation another time to feel better about your situtation.")
    elif showPaths:
        print(f"All conversation routes for lesson set: '{lessons.name}'")
        print(lessons.conversationRoutes())
    else:
        usage()
