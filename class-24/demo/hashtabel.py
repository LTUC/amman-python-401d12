from linked_list import LinkedList

class Hashtabel():
    def __init__(self,size=3):
        self.size = size
        self.map = [None]*size

    def custom_hash(self, key):

        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        
        temp = sum_of_asccii * 599
        indx = temp%self.size
        return indx
    

    def set(self, key, value):

        hashed_key = self.custom_hash(key)

        if not self.map[hashed_key]: # if the Bucket is empty :
            self.map[hashed_key] = [key,value]
        else: # collision happened
            if isinstance(self.map[hashed_key], LinkedList):  #not at the first time
                self.map[hashed_key].add([key,value])
            else: # at the first time (chaining process)
                chain = LinkedList()
                exsisting_pair = self.map[hashed_key]
                new_pair = [key,value]

                self.map[hashed_key] = chain
                chain.add(exsisting_pair)
                chain.add(new_pair)







    

