import json
import lib.defines as df

# json文件


def get_day() -> int:
    try:
        with open(df.day_json_file, "r") as f:
            data = json.load(f)
    except:
        data = {}
    try:
        day = data["day"]
    except KeyError:
        print("data中没有day   data：", data)
        data.update({"day": 0})
        day = 0
    return day


def get_user_data() -> dict:
    """获取用户数据，即公共仓库中 的物品数量"""
    try:
        with open(df.goods_json_file, "r") as f:
            goods = json.load(f)
            """各种商品的数量"""
    except:
        goods = {}
    return goods


def set_user_data(goods: dict) -> None:
    """写入用户数据，即公共仓库中的 good 数量"""
    with open(df.goods_json_file, "w") as f:
        json.dump(goods, f)

