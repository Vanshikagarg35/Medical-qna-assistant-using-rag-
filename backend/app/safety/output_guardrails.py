import re
UNSAFE=[r'you definitely have',r'you are diagnosed',r'i prescribe',r'take \d+\s*(mg|ml)',r'guaranteed cure',r'do not see a doctor']
def is_safe_output(text):return not any(re.search(p,text.lower()) for p in UNSAFE)
