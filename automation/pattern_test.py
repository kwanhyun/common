import re

sample_string = "{cert_path}"
origin = "sdfsdfdsf#{cert_path}#sdfsdf"
pattern  = r"^.*#{cert_path}#.*$"
if re.match(pattern,origin):
    print("good"+origin)
else:
    print("not good"+origin)



