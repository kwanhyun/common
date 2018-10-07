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

#config 정보 불러오는 함수
dictionary_config = {}
def get_config_list():
    with open(ConfigDir_Main+"values.txt") as f:
        for line in f:
            (key,val) = line.rstrip("\n").replace(" ","").split('=')
            dictionary_config[str(key)]=val
    for key, value in dictionary_config.items():
        print(key+' is ' + value)

#compare string values
def convert_valiable(str_info):
    origin = str_info
    pattern  = r"^.*#{.*}#.*$"  
    if re.match(pattern,origin):
        for key, value in dictionary_config.items():    
            if key in origin:
                print ('before: ' +origin)
                result=origin.replace(key,value)
                print ('after: ' +result)
                return result
    else:
        return origin
        
#Main
with open("server_config_test.xml","rt",encoding=None) as f:
    get_config_list()
    for line in f:
        new_line = convert_valiable(line)
        with open("new_server_config_test1"+dt+".xml","a") as f:
            f.write(new_line)
            f.close()
    f.close()
