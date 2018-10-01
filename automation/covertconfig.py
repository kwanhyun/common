from shutil import copyfile
import datetime
import re
import os

now_time=datetime.datetime.now()
dt=now_time.strftime('%Y%m%d_%H%M%S')

currentDir = os.path.dirname(os.path.abspath(__file__))
bnsBackupDir_Main = currentDir+"\\BackupDir\\"
ConfigDir_Main = currentDir+"\\Config_Value\\"
#backup config file
copyfile("server_config_test.xml",bnsBackupDir_Main+"server_config_test_.xml_"+dt)

#함수를 만들어서.. 

def convert_valiable(str_info):
    origin = str_info
    pattern  = r"^.*#{.*}#.*$"
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

dictionary_config = {}
with open(ConfigDir_Main+"values.txt") as f:
    for line in f:
        (key,val) = line.replace(" ","") .split('=')
        dictionary_config[str(key)]=val
        #print(dictionary_config['#{cert_path}#'])

#Send-Email

#def parsing_config(str_info):
#    origin_val = str_info
#    m = re.search()





