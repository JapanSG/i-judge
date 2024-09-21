'''Digital'''
def to_bool(string:str)-> bool:
    '''Return True/False based on "Yes"/"No"'''
    if string in ["Yes","True"]:
        return True
    return False
def main():
    '''Driver Code'''
    name = input()
    is_thai = to_bool(input())
    is_in_thailand = to_bool(input())
    age = float(input())
    income = float(input())
    saving = float(input())
    if not is_thai or not is_in_thailand or age < 16 or saving > 500000 or income > 840000:
        print(f"Unfortunately, {name} is not qualified.")
        return
    print(f"Congratulations! {name} is qualified to receive a \
digital wallet amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    return
main()
