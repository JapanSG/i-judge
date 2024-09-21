'''Ping'''
def get_ip(line):
    '''get ip'''
    left = 0
    right = 0
    brackets = False
    length = len(line)
    for i in range(length):
        if line[i] == "[":
            brackets = True
            left = i+1
        if line[i] == "]":
            brackets = True
            right = i
    if not brackets:
        for i in range(length):
            if line[i].isdigit() and line[i+1].isdigit() and line[i+2].isdigit():
                left = i
                while line[i] != " ":
                    i += 1
                right = i
                break
    return line[left:right]
def main():
    '''Driver Code'''
    input()
    input()
    line = input()
    ip = get_ip(line)
    least = 10000
    most = -1
    total,received = 0
    for _ in range(4):
        line = input()
        j = line.find("time")+4
        num = ""
        if line[j] == "<":
            num = "0"
        elif line[j] == "=":
            j +=1
            while line[j].isdigit():
                num += line[j]
                j += 1
        if len(num) > 0:
            least = min(least,int(num))
            most = max(most,int(num))
            total += int(num)
            received += 1
        lost = 4 - received
        per = int(lost/4*100)
    print(f"Ping statistics for {ip}:")
    print(f"    Packets: Sent = 4, Received = {received}, Lost = {lost} ({per}% loss),")
    if received > 0:
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {least}ms, Maximum = {most}ms, Average = {total//received}ms")
main()
