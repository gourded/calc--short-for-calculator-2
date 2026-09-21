class Calculation:
    def __init__(self):
        self.nums = []
        self.opps = []
    def add_num(self, num):
        self.nums.append(num)
    def add_opp(self, opp):
        self.opps.append(opp)
    def calculate(self):
        nums = self.nums
        opps = self.opps
        if not nums:
            return 0 
        result = nums[0]
        i = 0
        while i < len(opps):
            if opps[i] == '*':
               nums[i] *= nums[i + 1]
               nums.pop(i + 1)
               opps.pop(i)
            elif opps[i] == '/':
                nums[i] /= nums[i + 1]
                nums.pop(i + 1)
                opps.pop(i)
            else:
                i += 1
        for i in range(len(opps)):
            if opps[i] == '+':
                result += nums[i + 1]
            elif opps[i] == '-':
                result -= nums[i + 1]
        return result