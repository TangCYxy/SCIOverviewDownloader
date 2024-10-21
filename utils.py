
import logs
import pyautogui
import math

max_color_distance = math.sqrt(3 * (255 ** 2))

def findColor(x1, y1, x2, y2, target_color, confidence):
    """
    避免框选了太大的图像，导致遍历像素点太麻烦（后期可以改并发）
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param target_color:
    :param confidence: 0-1
    :return:
    """
    img = pyautogui.screenshot(region=(x1, y1, x2, y2))
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # 判断相似度，计算欧式距离
            distance = math.sqrt((target_color[0] - r) ** 2 + (target_color[1] - g) ** 2 + (target_color[2] - b) ** 2)
            simularity = (1 - distance / max_color_distance)
            if simularity > confidence:
                return x, y
    return None, None
