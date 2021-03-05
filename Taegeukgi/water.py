from PIL import Image, ImageDraw
from .background import h, bg

# 감 = 물 = 지혜
water = Image.new('RGB', (h // 4, h // 6), color=(14, 14, 14))
draw = ImageDraw.Draw(water)

draw.rectangle((0, h * 2 // 48, h // 4, h * 3 // 48), fill=(241, 241, 241))
draw.rectangle((0, h * 5 // 48, h // 4, h * 6 // 48), fill=(241, 241, 241))
draw.rectangle((h * 11 // 96, 0, h * 13 // 96, h * 2 // 48), fill=(241, 241, 241)) # 1
draw.rectangle((h * 11 // 96, h * 6 // 48, h * 13 // 96, h * 8 // 48), fill=(241, 241, 241)) # 3

water = water.rotate(90 + 33.69, expand=True, fillcolor=(241, 241, 241))

bg.paste(water, (h * 96 // 96, h * 9 // 96))