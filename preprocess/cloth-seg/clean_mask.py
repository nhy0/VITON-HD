import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("--cloth", type=str, default="0")

args = parser.parse_args()

edge_path='output_images' + "/" + args.cloth
content_path='input_images' + "/" + args.cloth

#read the color
img_edge = cv2.imread(edge_path)
img_content = cv2.imread(content_path)
# 这两个直接相乘后会导致255×n溢出，产生不正常的颜色，所以要修改

#color inverse  ---> obtain the inverse edge color image
img_inverse_edge=255*np.ones_like(img_edge)-img_edge

#img0 consists of 0 and 1 color, otherwise it overflows
img0=img_edge/255

image=img0*img_content+img_inverse_edge
image=np.array(image,dtype=np.uint8)
cv2.imwrite(content_path, image)

