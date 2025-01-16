class linkNode:
    link = []
    index = -1

    def clear(self):
        self.link.clear()
        self.index = -1

    def set(self, value, child):
        self.index = 1
        self.link.extend([value, child])

    def get_next(self, item=None, direction=1, test=False):
        index = self.index

        if index + direction == len(self.link):
            if item != None and not test:
                self.link.append(item)
        elif item and index + direction < len(self.link):
            if not test:
                self.link[self.index + 1] = item

        index += direction

        if -1 < index < len(self.link):
            item = self.link[index]
            if not test:
                self.index = index
            return item
        else:
            return []

    def set_next(self, item):
        self.link[self.index + 1] = item
