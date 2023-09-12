import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['i']
img = cv2.imread(img_path)
print(img_path)