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
    def append(self,sub_str:str) -> None:
        '''Append substring'''
        self.string = self.string+sub_str
    def isalzero(self) -> bool:
        '''Check if string is all 0'''
        for i in self.string:
            if i != 0:
                return False
        return True
    def replace(self,old:str,new:str) -> None:
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
        for i in self.string:
            length += 1
        return length
def to_notation(num:String)->str:
    neg = ""
    if num.string[0] == "-":
        num.replace("-","")
        neg = "-"
    
    num.insert(".",1)
    power = len(num.string[2:])
    zero_index = len(num)-1
    for i in range(zero_index,-1,-1):
        if num[i] != "0":
            zero_index += 1
            break
        zero_index -= 1
    num.delete(zero_index+1,num.length()-1)
    return f"{neg}{num} x 10^{power}"
def main():
    '''Driver Code'''
    num = String("123000000")
    print(to_notation(num))
if __name__ == "__main__":
    main()
