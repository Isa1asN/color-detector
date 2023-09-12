import argparse
import cv2
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument('-i', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['i']
img = cv2.imread(img_path)
# print(img_path)

cols = ["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=cols, header=None)

cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_function)