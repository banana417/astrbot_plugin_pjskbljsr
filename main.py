from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import astrbot.api.message_components as Comp

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
            # 计算第一个结果（保留中间计算精度）
            sum_nums = num2 + num3 + num4 + num5
            result1 = num1 + sum_nums * 0.2
            
            # 计算第二个结果
            result2 = result1 * 0.01 + 1
            
            # 构造结果消息（所有数值保留两位小数）
            main_result = f"您的模拟卡组：倍率为{result2:.2f}:技能实际值为{result1:.2f}%"
            
            # 添加计算过程说明
            decorated_response = [
                Comp.Plain("🎮 Project SEKAI 倍率计算结果：\n"),
                Comp.Plain(f"• 主卡值: {num1:.2f}\n"),
                Comp.Plain(f"• 副卡值: {num2:.2f}, {num3:.2f}, {num4:.2f}, {num5:.2f}\n"),
                Comp.Plain(f"• 副卡总值: {sum_nums:.2f}\n"),
                Comp.Plain(f"• 技能实际值 = {num1:.2f} + {sum_nums:.2f}×0.2 = {result1:.2f}\n"),
                Comp.Plain(f"• 倍率值 = {result1:.2f}×0.01 + 1 = {result2:.2f}\n\n"),
                Comp.Plain("📊 " + main_result)
            ]
            
            # 发送结果
            yield event.chain_result(decorated_response)
        
        except ValueError:
            error_msg = "❌ 参数错误！请输入5个有效的数字\n格式：倍率 数字1 数字2 数字3 数字4 数字5\n示例：倍率 100 50 50 50 50"
            yield event.plain_result(error_msg)
        except Exception as e:
            logger.error(f"计算发生错误: {str(e)}")
            yield event.plain_result("⚠️ 计算过程中发生意外错误，请检查输入格式")
