""" RemoveTag """
import re
print(re.sub(r"<[^<>]*>" ,' ' , input()).split())
