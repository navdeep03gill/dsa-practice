class TimeMap:

    def __init__(self):
        self.struct = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        # just use array
        if key not in self.struct:
            self.struct[key] = []
        
        self.struct[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.struct.get(key, [])
        left = 0
        right = len(values) - 1

        res = ""

        while(left <= right):
            mid = (left + right) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res

             


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

obj = TimeMap()

inputArr = [["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
for i in range(len(inputArr)):
    input = inputArr[i]
    if len(input) == 3:
        res = obj.set(input[0], input[1], input[2])
        print(res)
    elif len(input) == 2:
        res = obj.get(input[0], input[1])
        print(res)
