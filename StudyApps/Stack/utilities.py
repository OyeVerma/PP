import random

class TopicAPI:
    def __init__(self, topic=False) -> None:
        self.topic = topic
        pass

    def inJson(self, text=False):
        d = {}
        lines = self.topic.text.splitlines() if self.topic else text.splitlines()
        d['title'] = lines[0] if lines[0][0] == '*' else f'Enter Your Title Here - {random.randint(99999, 999999)}'
        d['text'] = self.topic.text if self.topic else text
        topics = {}
        topic_key = ''
        for line in lines:
            line = line.strip()
            if line[0:1] == '-' and line[0:2] != '--':
                topics[line[1:]] = []
                topic_key = line[1:]
            elif line[0:2] == '--':
                topics[topic_key].append(line[2:])
        d.update({'topics':topics})
        return d

    def fromFile(self, file):
        file_name, file_text = file.name, file.read().decode()
        d = self.inJson(file_text)
        if d['title'] == '':
            d['title'] = file_name.replace(file_name.split('.')[-1], '')
        return d