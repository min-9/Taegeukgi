from PIL import Image, ImageDraw
from .background import h, bg

# 건 = 하늘 = 정의
sky = Image.new('RGB', (h // 4, h // 6), color=(14, 14, 14))
draw = ImageDraw.Draw(sky)

draw.rectangle((0, h * 2 // 48, h // 4, h * 3 // 48), fill=(241, 241, 241))
draw.rectangle((0, h * 5 // 48, h // 4, h * 6 // 48), fill=(241, 241, 241))

sky = sky.rotate(90 - 33.69, expand=True, fillcolor=(241, 241, 241))

bg.paste(sky, (h * 22 // 96, h * 9 // 96))