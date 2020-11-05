''''
The traffic light has a method called next_state that makes the following transitions:

Make sure that only one light at the time is on.
If no lights are on, turn the green light first.
Also, implement a method get_state to return the state of the 3 lights (whether they are on or off) as a string.
'''

if __name__ == "__main__":
    class TrafficLight:

        def __init__(self):
            self.green = False
            self.orange = False
            self.red = False
            self.is_upward = False

        def next_state(self):
            if self.green:
                self.green = False
                self.orange = True
            elif self.orange:
                self.orange = False
                if not self.is_upward:
                    self.red = True
                    self.is_upward = True
                else:
                    self.green = True
                    self.is_upward = False
            elif self.red:
                self.red = False
                self.orange = True
            else:
                self.green = True

        def get_state(self):
            res = ''
            if self.green:
                res = res + '\033[1m\033[92mO\033[0m'
            else:
                res = res + 'O'
            if self.orange:
                res = res + '\033[1m\033[93mO\033[0m'
            else:
                res = res + 'O'
            if self.red:
                res = res + '\033[1m\033[91mO\033[0m'
            else:
                res = res + 'O'
            return res

    l1 = TrafficLight()
    l1.get_state()
    for i in range(10):
        l1.next_state()
        print(l1.get_state())