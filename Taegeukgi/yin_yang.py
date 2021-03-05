from PIL import Image, ImageDraw
from .background import h, tgg

# 태극 문양 = 음양
yin_yang = Image.new('RGB', (h // 2, h // 2), color=(241, 241, 241))
draw = ImageDraw.Draw(yin_yang)

draw.pieslice((0, 0, h // 2, h // 2), start=180, end=360, fill=(205, 49, 58))
draw.pieslice((0, 0, h // 2, h // 2), start=0, end=180, fill=(0, 71, 160))

draw.ellipse((0, h // 8, h // 4, h * 3 // 8), fill=(205, 49, 58))
draw.ellipse((h // 4, h // 8, h // 2, h * 3 // 8), fill=(0, 71, 160))

yin_yang = yin_yang.rotate(-33.69, fillcolor=(241, 241, 241))

tgg.paste(yin_yang, (h // 2, h // 4))