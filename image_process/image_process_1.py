import cv2
import numpy as np


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


#(3) カラー画像を読み込み,グレースケール化した画像を別名で保存するプログラム
im_rgb = cv2.imread('image/berry.jpeg')
im_gray = cv2.cvtColor(im_rgb, cv2.COLOR_BGR2GRAY)
cv2.imwrite('image/berry_gray.jpg', im_gray)
print('(3)')
cv2.waitKey(0)

#(4) カラー画像を読み込み,3 チャネル(RGB)に分離し,入力画像と共に各チャネルの画像を表示するプログラム
im_bgr = cv2.imread('image/berry.jpeg')
im_b, im_g, im_r = cv2.split(im_bgr)

#グレー画像とカラー画像の合成のために,グレー画像をカラー化
im_b = cv2.cvtColor(im_b,cv2.COLOR_GRAY2BGR)
im_g = cv2.cvtColor(im_g,cv2.COLOR_GRAY2BGR)
im_r = cv2.cvtColor(im_r,cv2.COLOR_GRAY2BGR)

im_h_1 = cv2.hconcat([im_rgb, im_b])
im_h_2 = cv2.hconcat([im_g ,im_r])
im_v = cv2.vconcat([im_h_1, im_h_2])
cv2.imwrite('image/image_array.jpeg', im_v)

cv2.waitKey(0)


#(5) カラー画像を読み込み,RGB 成分を以下の数式に従い変換し,グレースケール化した画像を別名で保存するプログラム
#Y = 0.2126 R + 0.7152 G + 0.0722 B

im_bgr = cv2.imread('image/berry.jpeg')
im_gray = cv2.cvtColor(im_rgb, cv2.COLOR_BGR2GRAY)
im_b, im_g, im_r = cv2.split(im_bgr)

im_b = 0.0722 * im_b
im_g = 0.7152 * im_g
im_r = 0.2126 * im_r

im_fomula = im_b + im_r + im_g
cv2.imwrite('image/image_fomula.jpeg', im_fomula)


print('(5)')
cv2.waitKey(0)


# すべてウィンドウを閉じる
cv2.destroyAllWindows()