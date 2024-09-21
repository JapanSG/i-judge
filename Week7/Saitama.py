'''Saitama'''
def main():
    '''Driver Code'''
    pushup_goal = int(input())
    situp_goal = int(input())
    squad_goal = int(input())
    run_goal = int(input())
    pushup = int(input())
    situp  =int(input())
    run = int(input())
    squad = int(input())
    total_pushup, total_situp, total_squad, total_run, day = (0,)*5
    while (total_pushup < pushup_goal or total_situp < situp_goal
    or total_squad < squad_goal or total_run < run_goal):
        total_situp += situp
        total_pushup += pushup
        total_squad += squad
        total_run += run
        day += 1
    print(day)
if __name__ == "__main__":
    main()
else:
    print("NO")
    