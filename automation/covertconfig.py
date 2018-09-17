from shutil import copyfile
import datetime
import re

now_time=datetime.datetime.now()
dt=now_time.strftime('%Y%m%d_%H%M%S')

#backup config file
copyfile("server_config_test.xml","server_config_test_.xml_"+dt)

#함수를 만들어서.. 

def convert_valiable(str_info):
    origin = str_info
    pattern  = r"^.*#{cert_path}#.*$"
    if re.match(pattern,origin):
        print("good"+origin)
        return origin
    else:
        return origin

#validable convert
with open("server_config_test.xml","rt",encoding=None) as f:
    for line in f:
        new_line = convert_valiable(line)
        with open("new_server_config_test1.xml","a") as f:
            f.write(new_line)
            f.close()
    f.close()



#Send-Email






