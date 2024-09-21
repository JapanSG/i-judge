'''IT Business'''
def main():
    '''Driver Code'''
    savings = float(input())
    cash = float(input())
    error = 0
    while True:
        if error == 3:
            break
        command = input()
        if command[0] == "D":
            deposit_amount = float(command[2:])
            if deposit_amount > cash:
                error += 1
                continue
            cash -= deposit_amount
            savings += deposit_amount
            error = 0
        elif command[0] == "W":
            withdraw_amount = float(command[2:])
            if withdraw_amount > savings:
                error += 1
                continue
            cash += withdraw_amount
            savings -= withdraw_amount
            error = 0
        else:
            break
    print(f"{savings:.2f}")
    print(f"{cash:.2f}")
if __name__ == "__main__":
    main()
