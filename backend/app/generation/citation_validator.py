import re
def citations_valid(answer,source_count):
 ids=[int(x) for x in re.findall(r'\[(\d+)\]',answer)]
 return bool(ids) and all(1<=x<=source_count for x in ids)
