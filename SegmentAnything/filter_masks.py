# Plan is: for all folders inside the dataset masks:
import os, argparse
import numpy as np
import pandas as pd

argParser = argparse.ArgumentParser()
argParser.add_argument('-n', '--nameSet', help='insert name of the set you want to elaborate')
args = argParser.parse_args()

dirname = args.nameSet

count_empty = 0
items = 0

for dir in os.listdir(f'originalSAMasks/{dirname}'):
    if dir == '.DS_Store' or dir == 'masks' or dir == '.' or dir == '..': continue  # sad MacOS user
    # Import the file metadata.csv
    f = pd.read_csv(f'originalSAMasks/{dirname}/{dir}/metadata.csv')
    f.drop(['id', 'crop_box_x0', 'crop_box_y0', 'crop_box_w', 'crop_box_h'], axis=1,
           inplace=True)  # This is data I don't need

    # Analyze bound on the input pt (a square of 100x100 pixels centered on the center pt) and use IoU to filter further
    f.drop(f[f['area'] > 145000].index, inplace=True)  # Drop the ones which are reversed and some sure hands

    f.drop(f[f['point_input_y'] < 200].index, inplace=True)
    f.drop(f[f['point_input_x'] < 150].index, inplace=True)
    f.drop(f[f['point_input_y'] > 1000].index, inplace=True)

    correct_masks = list(f.index)
    print(dir, correct_masks)
    if len(correct_masks) == 0:
        count_empty = count_empty + 1
        items = items + 1
        continue
    else:
        correct_one = correct_masks[0]
    items = items + 1

    savepath = f'originalSAMasks/{dirname}/masks/'
    if not os.path.exists(savepath): os.makedirs(savepath)
    os.system(f'cp originalSAMasks/{dirname}/{dir}/{correct_one}.png {savepath}/{dir}.png')
    # for file in os.listdir(f'originalSAMasks/{dirname}/{dir}'):
    # found = False
    # for m in correct_masks:
    # if file == 'metadata.csv': break
    # if int(file[:-4]) == int(m):
    # found = True
    # break
    # if not found:
    # os.remove(f'originalSAMasks/{dirname}/{dir}/{file}')

print(f'I lose {count_empty} items over {items} total images')
