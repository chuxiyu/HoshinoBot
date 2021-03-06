import random
import asyncio

import nonebot

from .gacha import gacha_10_aliases, gacha_1_aliases
from hoshino.log import logger

ban_hb_title = []
ban_hb_title.extend(gacha_10_aliases)
ban_hb_title.extend(gacha_1_aliases)


bot = nonebot.get_bot()

@bot.on_message('group')
async def hb_handler(context):
    message = context['message']
    self_id = context['self_id']
    group_id = context['group_id']
    user_id = context['user_id']
    for m in message:
        if m['type'] == 'hb':
            try:
                title = m['data']['title']
                if title in ban_hb_title:
                    bot.set_group_ban(self_id=self_id, group_id=group_id, user_id=user_id, duration= 12*60*60)
                # sleep(0.5 + 3 * random.random())
                # await bot.send(context, title)
            except Exception as e:
                logger.error(f'hb_handler: {type(e)}')
