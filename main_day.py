import lib.function as fun
import json
import time
import lib.defines as df
import os
# json文件

while True:
    time.sleep(1.5)
    os.system("cls")
    day = fun.get_day() + 1
    with open(df.day_json_file, "w") as f:
        json.dump({"day": day}, f)
    print("day:", day)
    print("==" * 20)
    ###############################################
    goods = fun.get_user_data()
    print(goods)
    print()
