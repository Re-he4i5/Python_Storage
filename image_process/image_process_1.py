import cv2
import numpy as np
from matplotlib import pyplot as plt

#(1) カラー画像を読み込み，カラー表示するプログラム
im_rgb = cv2.imread('image/berry.jpeg')
cv2.imshow('image',im_rgb)
print('(1)')
cv2.waitKey(0)

#(2) カラー画像を読み込み，グレースケール表示するプログラム
im_gray = cv2.imread('image/berry.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',im_gray)
print('(2)')
cv2.waitKey(0)


#(3) カラー画像を読み込み，グレースケール化した画像を別名で保存するプログラム
im_rgb = cv2.imread('image/berry.jpeg')
im_gray = cv2.cvtColor(im_rgb, cv2.COLOR_BGR2GRAY)
cv2.imwrite('image/berry_gray.jpg', im_gray)
print('(3)')
cv2.waitKey(0)

#(4) カラー画像を読み込み，3 チャネル(RGB)に分離し，入力画像と共に各チャネルの画像を表示するプログラム
im_bgr = cv2.imread('image/berry.jpeg')

#cv2.imshow('image_b',im_b)
#cv2.imshow('image_g',im_g)
#cv2.imshow('image_r',im_r)
#BGRからRGBに変換
im_rgb = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)
im_r = im_rgb[:,:, 0]
im_g = im_rgb[:,:, 1]
im_b = im_rgb[:,:, 2]

plt.subplot(2, 2, 1)
plt.imshow(im_rgb)
plt.subplot(2, 2, 2)
plt.imshow(im_b) 
plt.subplot(2, 2, 3)
plt.imshow(im_g) 
plt.subplot(2, 2, 4)
plt.imshow(im_r) 
plt.show()
print('(4)')
cv2.waitKey(0)

im_bgr = cv2.imread('image/berry.jpeg')
im_r = im_bgr.copy()
im_r[:, :, (1, 2)] = 0
im_g = im_bgr.copy()
im_g[:, :, (0, 2)] = 0
im_b = im_bgr.copy()
im_b[:, :, (0, 1)] = 0

# 横に並べて結合（どれでもよい）
im_RGB = np.concatenate((im_r, im_g, im_b), axis=1)

plt.imshow(im_RGB)
print('(4-2)')
cv2.waitKey(0)


#(5) カラー画像を読み込み，RGB 成分を以下の数式に従い変換し，グレースケール化した画像を別名で保存するプログラム
#Y = 0.2126 R + 0.7152 G + 0.0722 B

im_bgr = cv2.imread('image/berry.jpeg')
im_b = im_bgr.copy()
im_b[:, :, (1, 2)] = 0
im_b = 0.0722 * im_bgr

im_g = im_bgr.copy()
im_g[:, :, (0, 2)] = 0
im_g = 0.7152 * im_bgr

im_r = im_bgr.copy()
im_r[:, :, (0, 1)] = 0
im_r = 0.2126 * im_bgr

im_fomula_RGB = im_b + im_r + im_g
cv2.imshow('image',im_b)


print('(5)')
cv2.waitKey(0)
# すべてウィンドウを閉じる
cv2.destroyAllWindows()