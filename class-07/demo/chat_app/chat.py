'''
small chat application to explain the oop principles
'''

'''
access modifiers:
Public: I can access the data from outside the class/module
Protected :(_) I can only access the data from the class/ the module or its children.
Private: (__) I can only access the data from the class.
'''

from uuid import uuid4
from abc import ABC, abstractmethod #Abstract Base Class

class Message(ABC):
    def __init__(self):
        self.__message_id = uuid4() # uuid module provides function for generating universally unique identifires
        self.sender = None
        self.receiver = None
        self.content = "Default Content" 

    @abstractmethod
    def confirm(self):
        pass

    # Setters & Getters Methods
    def set_sender(self,sender):
        self.sender = sender
        
    def set_receiver(self,receiver):
        self.sender = receiver

    def set_content(self,content):
        self.sender = content

    def get_sender(self):
        return self.sender
    
    def get_receiver(self):
        return self.receiver
    
    def get_content(self):
        return self.content
    
    def get_size():
        return "size is small"
    
    #overloading (magic methods)
    def __str__(self):
        return "Hello"

class AudioMessage(Message): #  AudioMessage class (child, sub class) inherts Message class (parent, super class)
    
    count = 0 # class attribuate

    def __init__(self, duration):
        super().__init__() # calling the init of the parent super class
        self.duration = duration
        AudioMessage.count += 1

    def trim(self):
        return "trim method will be added later"


    # overriding
    def confirm(self):
        return "confirmed !"
    
    def get_size(self):
        return "size is big"

    @classmethod
    def get_count(cls): # cls : class itself
        return AudioMessage.count
    

audio_msg = AudioMessage(3)
audio_msg2 = AudioMessage(4)

print(audio_msg.get_size())

print(AudioMessage.get_count())
    

        


