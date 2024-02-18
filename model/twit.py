from model.user import User

class Twit:
    
    
    def __init__ (self ,body : str, author : User):
        self.body = body
        self.author = author

    def to_json(self):
        return {'body':self.body, 'author':self.author}
        
        
