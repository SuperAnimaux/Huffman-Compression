

class File:

    def __init__(self):
        self.file = []

    def popfile(self):
        return self.file.pop(0)
    
    def insertfile(self, element):
        return self.file.append(element)
    
    def file_len(self):
        return len(self.file)
    
