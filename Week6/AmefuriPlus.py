'''Amefuri Plus'''
class Cloth:
    '''Cloth Class'''
    wetness  = 8
    lost = False
    def __init__(self,hour):
        '''Contructor'''
        self.hour = hour
        if 6 <= hour < 18:
            self.day = True
        else:
            self.day = False
    def time(self,weather):
        '''Move time forward by an hour and adjust wetness based on the weather'''
        weather = weather.lower()
        if self.day:
            bonus = 2
        else:
            bonus = 1
        if weather == "c":
            self.wetness -= 0.25*bonus
        elif weather == "n":
            self.wetness -= 0.5*bonus
        elif weather == "w":
            self.wetness -= 0.75*bonus
        elif weather == "r":
            self.wetness += 2
        elif weather == "s":
            self.wetness += 3
        else:
            self.lost = True
        self.hour += 1
        if self.hour >= 24:
            self.hour = 0
        if self.wetness < 0:
            self.wetness = 0
        if self.wetness > 16:
            self.wetness = 16
        return self.wetness
    def is_dry(self):
        '''Check if cloth is dry'''
        if self.wetness <= 0:
            return True
        return False
    def is_lost(self):
        '''Check if cloth is lost'''
        if self.lost:
            return True
        return False
    def update_time(self):
        '''Update day and night'''
        if 6 <= self.hour < 18:
            self.day = True
        else:
            self.day = False
def main():
    '''Driver Code'''
    hour = int(input())
    weather_pattern = input()
    cloth = Cloth(hour)
    for n in weather_pattern:
        cloth.time(n)
        cloth.update_time()
        if cloth.is_lost():
            return "Lost"
        if cloth.is_dry():
            return "Dry"
    return f"Still Wet (Wet Level: {cloth.wetness:.2f})"
print(main())
