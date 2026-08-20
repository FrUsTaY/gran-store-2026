with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# I will update "Коллекции" products as well, there are 4 of them in the HTML.
# But wait, the task doesn't explicitly mention to update them to anything specific,
# but it says "заменив все `picsum.photos` и вымышленные названия на реальные данные".
# Does the task have 18 items or 22 items? The layout map (1.png) only had 18 items.
# Let's check how many picsum.photos are still there.
