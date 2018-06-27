import yaml
import re

class Matcher:
    def __init__(self, path):
        self.file = open(path, 'r+')
        try:
            self.metadata = yaml.load(self.file)
            self.keys = list(self.metadata.keys())
            self.file.seek(0, 0)
        except yaml.YAMLError as err:
            print(err)

    def __str__(self):
        return yaml.dump(self.metadata, default_flow_style=False)

    def cleanup(self):
        self.file.close()

    def save(self):
        try:
            self.file.write(str(self))
            self.file.seek(0, 0)
        except IOError as err:
            print(err)

    def getExactMatch(self, key):
        if key in self.metadata:
            return self.metadata[key]
        else:
            return None

    def getRegexMatch(self, expression):
        regex = re.compile(expression)
        keys = filter(regex.search, self.keys)
        return list(map(lambda k: self.metadata[k], keys))

    def setMatch(self, key, match):
        if not key in self.metadata:
            self.keys += [key]
        self.metadata[key] = match
        self.save()
