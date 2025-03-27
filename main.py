from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from .randomzb import get_random_numbers

@register("sjzb", "灵煞", "一个输出绝地潜兵随机战备插件", "1.0.1")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    # 注册指令的装饰器。指令名为 sjzb。注册成功后，发送 `/sjzb` 就会触发这个指令，一组战备`
    @filter.command("sjzb")
    async def sjzb(self, event: AstrMessageEvent):
        jg = get_random_numbers()
        yield event.plain_result(f"{jg}") # 发送一条纯文本消息
