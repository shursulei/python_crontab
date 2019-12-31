#encoding:utf-8
from PropertiesUtil import Properties
import crontba2
import sys,os
import time

def getFiles(dir, suffix):  # 查找根目录，文件后缀
    res = []
    for root, directory, files in os.walk(dir):  # =>当前根,根下目录,目录下的文件
        for filename in files:
            name, suf = os.path.splitext(filename)  # =>文件名,文件后缀
            if suf == suffix:
                res.append(name)
    return res

if __name__ == '__main__':
    for file in getFiles("./", '.properties'):  # =>查找以.py结尾的文件
        user = file[len("global_"):len(file)].replace("\n", "")
        properties_file = file + ".properties"
        if user is not None and properties_file is not None:
            dictProperties=Properties(properties_file).getProperties()
            time_stamp = int(time.time())
            # print time_stamp
            for conf_string,system_command in dictProperties.items():
                    res, desc=crontba2.parse_crontab_time(conf_string)
                    if res == 0:
                        cron_time = desc
                    else:
                        sys,exit(-1)
                    time_struct = crontba2.get_struct_time(time_stamp)
                    match_res = crontba2.time_match_crontab(cron_time, time_struct)
                    # print  match_res
                    if (match_res[1]):
                        if user=="root":
                            os.system(system_command);
                        else:
                            os.system("su - "+user+"-c '"+system_command+"' ");



