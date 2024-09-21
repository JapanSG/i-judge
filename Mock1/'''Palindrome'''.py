'''Palindrome'''
def to_string(time):
    '''tosring'''
    string = ""
    for i in time:
        if i.isdigit():
            string += i
    return string
def get_hour(time):
    '''asd'''
    hour = ""
    i = 0
    while time[i] != ":":
        hour += time[i]
        i += 1
    return hour
def time_incre(time):
    '''asdjgauwdg'''
    time = time[:-2]+f"{int(time[-2:])+1:02d}"
    if time[-2:] == "60":
        hour = get_hour(time)
        hour = f"{int(hour)+1}"
        time = f"{hour}:00"
    if get_hour(time) == "24":
        time = "0:00"
    return time
def main():
    """Driver Code"""
    num = int(input())
    time = input()
    time = time_incre(time)
    printed = 0
    while printed < num:
        if to_string(time) == to_string(time)[::-1]:
            print(time)
            printed += 1
        time = time_incre(time)
main()
