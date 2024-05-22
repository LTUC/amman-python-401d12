from abc import ABC, abstractmethod
from typing import List
import uuid
import random
from enum import Enum


class TicketCategory(Enum):
    LAB = 1
    CODE_CHALLENGE = 2
    GENERAL_QUESTION = 3

class Ticket:
    def __init__(self, category, username, des, course_name):
        self.id = uuid.uuid4()
        self.category = category
        self.username = username
        self.des = des
        self.course_name = course_name

#1 Strategy Interface
class Strategy(ABC):
    @abstractmethod
    def create_ordering(self, list : List[Ticket]) -> List[Ticket]:
        pass

#2 concrete classes

class FIFOOrderingStrategy(Strategy):
    def create_ordering(self, list: List[Ticket]) -> List[Ticket]:
        return list.copy()
    
class FILOOrderingStrategy(Strategy):
    def create_ordering(self, list: List[Ticket]) -> List[Ticket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy
    
class RandomOrderingStrategy(Strategy):
    def create_ordering(self, list: List[Ticket]) -> List[Ticket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy

# 3 Context Class   
class Context():
    def __init__(self, strategy):
        self.strategy = strategy
        self.tickets = []

    def add_ticket_to_queue(self, category, username, des, course_name):
        new_ticket = Ticket(category, username, des, course_name)
        self.tickets.append(new_ticket)

    def set_strategy(self, strategy : Strategy):
        self.strategy = strategy

    def process_tickets(self):
        # call the chared method from the strategy that we have passed
        ticket_list = self.strategy.create_ordering(self.tickets)

        if len(ticket_list) == 0:
            print("There are no tickets !")
            return
        for ticket in ticket_list:
            self.process_single_ticket(ticket)

    def process_single_ticket(self, ticket : Ticket):
        print("=============================")
        print(f"Processing Ticket ID: {ticket.id}")
        print(f"Student Name: {ticket.username}")
        print(f"Des: {ticket.des}")
        print(f"Course Name: {ticket.course_name}")
        print(f"Category: {ticket.category}")

if __name__ == "__main__":
    context = Context(FIFOOrderingStrategy())
    context.add_ticket_to_queue(TicketCategory.LAB.name, "Roaa", "problem in lab 09", "401d12")
    context.add_ticket_to_queue(TicketCategory.CODE_CHALLENGE.name, "Mkarem", "problem in cc 09", "401d12")
    context.add_ticket_to_queue(TicketCategory.GENERAL_QUESTION.name, "Raghad", "general question", "401d10")

    context.process_tickets()

    # print("+++++++++++++++++++++++++++++")
    # context.set_strategy(RandomOrderingStrategy())
    # context.process_tickets()