'''Scientific Notation'''
class String(str):
    '''String Wrapper Class'''
    string = ""
    def __init__(self,string:str) -> None:
        '''Constructor'''
        self.string = string
    def __str__(self) -> str:
        '''Return String object attribute for printing'''
        return self.string
    def insert(self,sub_str:str,index:int) -> None:
        '''Adds substring at index'''
        self.string = self.string[:index]+sub_str+self.string[index:]
    def isalzero(self) -> bool:
        '''Check if string is all 0'''
        for i in self.string:
            if i not in ["0","."]:
                return False
        return True
    def replace_(self,old:str,new:str) -> None:
        '''Replace all old substring with new substring'''
        old_len = len(old)
        new_len = len(new)
        left = 0
        right = old_len-1
        while right < len(self.string):
            if self.string[left:right+1] == old:
                self.string = self.string[:left]+new+self.string[right+1:]
                left += new_len
                right += new_len
            else:
                left += 1
                right += 1
    def delete(self,left:int,right:int) -> None:
        '''Delete charater between two index range'''
        self.string = self.string[:left]+self.string[right+1:]
    def length(self)->int:
        '''Return string length'''
        length = 0
        for _ in self.string:
            length += 1
        return length
def to_notation(num:String)->str:
    '''to notation'''
    if num.isalzero():
        return 0
    neg = ""
    if num.string[0] == "-":
        num.replace_("-","")
        neg = "-"
    if "." in num:
        if num.string[0] == "0":
            new = String(num.string[2:])
            power = 1
            for i in new.string:
                if i != "0":
                    break
                power += 1
            new = String(new.string[power-1:])
            new.insert(".",1)
            if new.length() == 2:
                new.string = new.string[0]
            return f"{neg}{new} x 10^-{power}"
        point = num.string.find(".")
        power = String(num.string[:point]).length()-1
        new = String(num.string[:point]+num.string[point+1:])
        new.insert(".",1)
        return f"{neg}{new} x 10^{power}"
    num.insert(".",1)
    power = len(num.string[2:])
    zero_index = len(num)-1
    for i in range(zero_index,-1,-1):
        if num[i] != "0":
            zero_index += 1
            break
        zero_index -= 1
    num.delete(zero_index+1,num.length()-1)
    if num.length() == 2:
        num.string = num.string[0]
    return f"{neg}{num} x 10^{power}"

def to_num(notation : str)->float:
    '''Return num'''
    neg = ""
    if notation[0] == "-":
        notation = notation[1:]
        neg = "-"
    if "." in notation and notation[0] == "0":
        power = int(notation[notation.find("^")+1:])
        right = String(notation[2:notation.find(" ")])
        if power < 0:
            new = notation[:notation.find('.')]+notation[notation.find('.')+1:notation.find(' ')]
            new = f"{'0'*abs(power)}"
            new = String(new)
            new.insert(".",1)
            return f"{neg}{new}"
        if right.length() <= power:
            right.string = f"{right.string}{'0'*(power-right.length())}"
        else:
            right.insert(".", power)
        for i in range(right.length()):
            if right.string[i] != "0":
                zero_index = i
                break
        right.delete(0,zero_index-1)
        if right.string[0] == ".":
            right.insert("0",0)
        return f"{neg}{right}"
    if "." in notation:
        left = notation[:notation.find(".")]
        right = notation[notation.find(".")+1:notation.find(" ")]
        power = int(notation[notation.find("^")+1:])
        places = len(right)
        if power < 0:
            ans = f"{'0'*(abs(power))}{left}{right}"
            ans = f"{neg}{ans[0]}.{ans[1:]}"
            return ans
        if power - places < 0:
            a = f"{left}{right}"
            a = String(a)
            a.insert(".",power+1)
            return f"{neg}{a.string}"
        return f"{neg}{left}{right}{'0'*(power-places)}"
    power = int(notation[notation.find("^")+1:])
    if power < 0:
        new = '0'*(abs(power)-len(notation[:notation.find(' ')])+1)+notation[:notation.find(' ')]
        new = String(new)
        new.insert(".",1)
        return f"{neg}{new}"
    return f"{neg}{notation[0:notation.find(' ')]}{'0'*power}"
def main():
    '''Driver Code'''
    num = String(input())
    if "x" in num.string:
        print(to_num(num.string))
    else:
        print(to_notation(num))
if __name__ == "__main__":
    main()
