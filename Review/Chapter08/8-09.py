class Queue:
    def __init__(self):
        self.q = []
    
    def isEmpty(self):
        return (len(self.q) == 0)

    def enqueue(self, item):
        return self.q.append(item)
    
    def dequeue(self):
        '''큐 맨 앞의 항목을 제거하고 반환
            만약 큐가 비어있으면 KeyboardInterrupt 예외가 발생'''
        if len(self)==0:
            raise KeyboardInterrupt('dequeue from empty queue')
            
        return self.q.pop(0)