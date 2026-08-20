import re
import random

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's replace the other picsum.photos with random images from assets/images/
images = [f"{i}.jpg" if i not in [1, 2, 11, 12, 17] else f"{i}.png" for i in range(1, 20)]

def replace_picsum(match):
    img = random.choice(images)
    return f'assets/images/{img}'

new_content = re.sub(r'https://picsum\.photos/id/\d+/\d+/\d+', replace_picsum, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replaced remaining picsum.photos with local assets.")
