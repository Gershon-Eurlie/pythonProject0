#def sqsum(nums):
#    return sum(x**2 for x in nums if x>0)

class FunEvent:
    def __init__(self, tags, year):
        self.tags = tags
        self.year = year

    def __str__(self):
        return f"FunEvent(tags={self.tags}, year={self.year})"

tags = ["Best", "ML Engineer"]
year = 2022
bootcamp = FunEvent(tags, year)
tags.append("I am going global")
year = 2023
print(bootcamp)