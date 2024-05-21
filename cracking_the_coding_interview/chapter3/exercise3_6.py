from collections import deque

class Shelter:

    def __init__(self):
        self.all_queue = []
        self.dog_queue = []
        self.cat_queue = []

    def __str__(self):
        print('-'.join(self.all_queue))
        dog_cnt, cat_cnt = 0, 0
        str_ = ''
        for animal in self.all_queue:
            if animal == 'dog':
                str_ += self.dog_queue[dog_cnt] + '-'
                dog_cnt += 1
            elif animal == 'cat':
                str_ += self.cat_queue[cat_cnt] + '-'
                cat_cnt += 1
        return str_[:-1]

    def enqueue(self, name, animal):
        if animal == 'dog':
            self.dog_queue.append(name)
        elif animal == 'cat':
            self.cat_queue.append(name)
        else:
            print('Enqueue dog or cat.')
            return
        self.all_queue.append(animal)
        
    def dequeueAny(self):
        if self.all_queue[0] == 'dog':
            self.all_queue.pop(0)
            return self.dog_queue.pop(0)
        elif self.all_queue[0] == 'cat':
            self.all_queue.pop(0)
            return self.cat_queue.pop(0)
   
    def dequeueDog(self):
        self.all_queue.remove('dog')
        return self.dog_queue.pop(0)

    def dequeueCat(self):
        self.all_queue.remove('cat')
        return  self.cat_queue.pop(0)

if __name__ =='__main__':
    slt = Shelter()
    a = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg']
    b = ['dog', 'cat', 'dog', 'dog', 'cat', 'cat', 'dog']
    for name, animal in zip(a, b):
        slt.enqueue(name, animal)

    print(slt)
    print('')
    print('dequeueAny', slt.dequeueAny())
    print(slt)
    print('')
    print('dequeueDog', slt.dequeueDog())
    print(slt)
    print('')
    print('dequeueDog', slt.dequeueDog())
    print(slt)
    print('')
    print('dequeuCat', slt.dequeueCat())
    print(slt)
    print('')
    print('dequeueAny', slt.dequeueAny())
    print(slt)
    print('')
    print('enqueue', 'hhh', 'cat')
    slt.enqueue('hhh', 'cat')
    print(slt)
    print('')
    print('dequeueDog', slt.dequeueDog())
    print(slt)
    print('')
    print('enqueue', 'iii', 'dog')
    slt.enqueue('iii', 'dog')
    print(slt)