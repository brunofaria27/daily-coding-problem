'''
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
- record(order_id): adds the order_id to the log
- get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
'''
class Order:
    def __init__(self):
        self.ids_log = list()

    def record(self, order_id):
        self.ids_log.append(order_id)

    def get_last(self, i):
        if i <= len(self.ids_log):
            return self.ids_log[len(self.ids_log) - i]
        else:
            return 'Not possible'

if __name__ == "__main__":
    commerce = Order()
    # Add a order in list
    for i in range(0, 30):
        commerce.record(i)
    
    assert commerce.get_last(30) == 0
    assert commerce.get_last(31) == 'Not possible'
    assert commerce.get_last(15) == 15

# Complexity Analysis
# Space Complexity: O(1)
# Time Complexity: O(1)
