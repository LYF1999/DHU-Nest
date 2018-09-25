from utils.ESModel import ESModel


class Post(ESModel):

    def __init__(self, id: str, title: str, author: int, content: str, created_time, updated_time, active_time):
        self.title = title
        self.id = id
        self.author = author
        self.content = content
        self.created_time = created_time
        self.updated_time = updated_time
        self.active_time = active_time
