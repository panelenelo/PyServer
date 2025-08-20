#Task class
from pydantic import BaseModel
from typing import Optional,List

class Task:
    def __init__(self, id: int,title: str, description: str, is_complete: bool):
        self.id = id
        self.title = title
        self.description = description
        self.is_complete = is_complete

    def switch_complete():
        is_complete = not(is_complete)

    def get_Title(self):
        return self.title

    def get_id(self):
        return self.id
    
    def get_description(self):
        return self.description
    
    def get_completion(self):
        return self.is_complete
