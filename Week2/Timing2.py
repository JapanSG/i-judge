"""TimingII"""
def main():
    """Driver code"""
    sec = int(input())
    minute = sec//60
    sec = sec%60
    hour = minute//60
    minute = minute%60
    day = hour//24
    hour = hour%24
    if not day//10000:
        print(f"{day:>04d}:{hour:02d}:{minute:02d}:{sec:02d}")
    else:
        print("ERR_:__:__:__")
main()
