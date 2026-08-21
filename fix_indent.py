with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if line.strip() == "</div>" and lines[i-1].strip() == "</div>" and lines[i+1].strip() == "</div>":
        pass # wait I can just check indentation

# Instead of python, let's just use plan_step_complete as it's fully functional now.
