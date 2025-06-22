from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register(
    "astrbot_plugin_pjskbljsr",
    "bunana417",
    "Project SEKAI 倍率计算插件",
    "1.0.0",
    "https://github.com/banana417/astrbot_plugin_pjskbljsr"
)
class PJSKBljsrPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    @filter.command("倍率")
    async def calculate_bljsr(self, event: AstrMessageEvent, num1: float, num2: float, num3: float, num4: float, num5: float):
        """
        Project SEKAI 倍率计算器
        格式: 倍率 数字1 数字2 数字3 数字4 数字5
        计算: 结果1 = 数字1 + (数字2+数字3+数字4+数字5)*0.2
             结果2 = 结果1 * 0.01 + 1
        输出: 您的模拟卡组：倍率为结果2:技能实际值为结果1%
        """
        try:
            # 计算副卡总和
            sum_nums = num2 + num3 + num4 + num5
            
            # 计算技能实际值
            result1 = num1 + sum_nums * 0.2
            
            # 计算倍率值
            result2 = result1 * 0.01 + 1
            
            # 构造并返回最终结果
            result_str = f"您的模拟卡组：倍率为{result2:.2f}:技能实际值为{result1:.2f}%"
            yield event.plain_result(result_str)
        
        except ValueError:
            yield event.plain_result("❌ 参数错误！请输入5个有效的数字\n格式：倍率 数字1 数字2 数字3 数字4 数字5")
        except Exception as e:
            logger.error(f"计算错误: {str(e)}")
            yield event.plain_result("⚠️ 计算过程中发生错误，请检查输入格式")
