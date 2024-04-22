import re
import os
import json
#iterate through folders
total = 0
img_total = 0
img_correct = 0
vid_total = 0
vid_correct = 0
correct = 0
filepath = 'Gemini/GeminiCoCoT.json'

with open(f'filepath', 'r') as file:
    data = json.load(file)

    for a in data:
        passed = False
        img_idx =  a['answer']
        if a['label'] in a['answer']:
            passed = True
        else:
            m = re.search(r"The answer is (Image [12])", a['response'])
            passed = True if m and a['label'] in m.group(0) else False
        img_dir = parts = a['img1'].split("/")[-2]
        if passed:
            correct += 1
        if 'open-images' in img_dir:
            img_total += 1
            if passed:
                img_correct += 1
        else: 
            vid_total += 1
            if passed:
                vid_correct += 1

        total += 1

print('OVERALL ACC: ' + str(round(correct/total,4)))
print('VIDEO ACC: ' + str(round(vid_correct/vid_total,4)))
print('IMG ACC: ' + str(round(img_correct/img_total,4)))