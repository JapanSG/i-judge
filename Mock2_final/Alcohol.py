'''Alcohol'''
def bool_gender(string:str) -> bool:
    '''return True if string == male else return False'''
    if string == "Male":
        return True
    return False
def bool_yes(string:str) -> bool:
    '''Return True if yes else return no'''
    if string == "Yes":
        return True
    return False
def main():
    '''Driver Code'''
    is_male = bool_gender(input())
    weight = float(input())
    have_lic = bool_yes(input())
    volumn = float(input())
    alcohol_percent = float(input()) #percent
    bottle = int(input())
    time = int(input())
    if not have_lic:
        print("Not Safe")
    else:
        alcohol = alcohol_percent/100*volumn*bottle
        val = 0.55
        if is_male:
            val = 0.68
        blood_alcohol = alcohol/(weight*val*10)*1000-15*time
        
        if blood_alcohol > 50:
            print("Not Safe")
        else:
            print("Safe")
main()
