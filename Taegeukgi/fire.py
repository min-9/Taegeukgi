from PIL import Image, ImageDraw
from .background import h, bg

# 이(리) = 불 = 결실
fire = Image.new('RGB', (h // 4, h // 6), color=(14, 14, 14))
draw = ImageDraw.Draw(fire)

draw.rectangle((0, h * 2 // 48, h // 4, h * 3 // 48), fill=(241, 241, 241))
draw.rectangle((0, h * 5 // 48, h // 4, h * 6 // 48), fill=(241, 241, 241))
draw.rectangle((h * 11 // 96, h * 3 // 48, h * 13 // 96, h * 5 // 48), fill=(241, 241, 241)) # 2

fire = fire.rotate(90 + 33.69, expand=True, fillcolor=(241, 241, 241))

bg.paste(fire, (h * 22 // 96, h * 59 // 96))