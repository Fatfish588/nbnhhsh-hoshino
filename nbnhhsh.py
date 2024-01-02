import re

import requests

from hoshino import Service
from hoshino.typing import CQEvent

sv = Service(
    name="能不能好好说话",  # 功能名
    visible=True,  # 可见性
    enable_on_default=True,  # 默认启用
    bundle="娱乐",  # 分组归类
    help_="发送【缩写nbnhhsh是什么意思】触发，其中的英文缩写就是要查询的内容",  # 帮助说明

)

host = "https://lab.magiconch.com/api/nbnhhsh/guess"
header = {'Content-Type': 'application/json'}


def extract_alphanumeric(text):
    pattern = r'[A-Za-z0-9]+'
    matches = re.findall(pattern, text)
    return str(matches[0])


def format_list(lst):
    result = ''
    if len(lst) > 0:
        for index, item in enumerate(lst, 1):
            result += f"{index}、{item}\n"
        return result
    else:
        return "emt"


async def request_url(text):
    response = requests.post(headers=header, json={"text": str(text)}, url=host).json()
    return response[0].get("trans")


@sv.on_rex(r'^缩写([a-zA-Z0-9]+)是什么意思[.,。?？]?$')
async def can_you_speak_well(bot, ev: CQEvent):
    user_message = str(ev.message)
    suo = extract_alphanumeric(user_message)
    res = await request_url(suo)
    if res is None:
        await bot.send(ev, f"'{suo}'未能查询到可能的解释", at_sender=False)
    else:
        formatted_res = format_list(res)
        result = f"'{suo}'有以下可能的意思：\n{formatted_res}"
        await bot.send(ev, result, at_sender=False)
