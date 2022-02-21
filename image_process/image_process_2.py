import cv2
from PIL import Image


#※ (1)~(15)はグレースケール画像を利用すること。
#※ 処理後の画像を別名で保存する処理も含めること)


#(1)画像の最大値，最小値，平均値を求めるプログラム
im = cv2.imread('image/berry.jpeg', cv2.IMREAD_GRAYSCALE)
height, width = im.shape
max = 0
min = 0
sum = 0
for y in range(height):
    for x in range(width):
        if max < im[y, x]:
            max = im[y, x]

for y in range(height):
    for x in range(width):
        if min > im[y, x]:
            min = im[y, x]

for y in range(height):
    for x in range(width):
        sum += im[y, x]

mean = sum/(height * width)

print('-------(1)------------')
print(max)
print(min)
print(mean)
print('-------(1)------------')

#(2)画像を左右反転するプログラム
im = cv2.imread('image/berry_gray.jpg')
img_flip_lr = cv2.flip(im, 1)
cv2.imwrite('image/im_flip_lr.jpeg', img_flip_lr)

#(3)画像を上下反転する作成プログラム
img_flip_ud = cv2.flip(im, 0)
cv2.imwrite('image/im_flip_ud.jpeg', img_flip_ud)

#(4)cv2.resize により画像を拡大縮小するプログラム(最近傍補間・バイリニア補間・平均画素法等)
im = cv2.imread('image/berry_gray.jpg')
#最近傍補間
im_resize_NEAREST = im.resize((height/2, width/2), interpolation=cv2.INTER_NEAREST)
cv2.imwrite('image/m_resize_NEAREST.jpeg', im_resize_NEAREST)
#バイリニア補間
im_resize_LINEAR = im.resize((height/2, width/2), interpolation=cv2.INTER_LINEAR)
cv2.imwrite('image/im_resize_LINEAR.jpeg', im_resize_LINEAR)
#平均画素法等
im_resize_AREA = im.resize((height/2, width/2), interpolation=cv2.INTER_AREA)
cv2.imwrite('image/im_resize_AREA.jpeg', im_resize_AREA)


#(5)PIL により画像を拡大・縮小するプログラム


#(6)アフィン変換により画像を拡大・縮小するプログラム

#(7)アフィン変換により，画像を平行移動するプログラム。

#(8)アフィン変換により，画像を回転するプログラム

#(9)輝度値(ピクセル値)のヒストグラムを作成するプログラム

#(10)輝度値(ピクセル値)のヒストグラムを平滑化(平準化)した画像の作成プログラム

#(11)ガウシアンフィルタにより平滑化するプログラム

#(12)sobel フィルタによるエッジ抽出プログラム

#(13)2 次微分フィルタによるエッジ抽出プログラム

#(14)画像を 2 値化(任意のしきい値)するプログラム


#(15)大津の 2 値化により画像を 2 値化するプログラム

#(16)2 値画像を田村のアルゴリズムにより細線化するプログラム

#(17)2 値画像を Zhang Suen のアルゴリズムにより細線化するプログラム

#(18)2 値画像の輪郭線抽出プログラム


#(19)カラー画像を読み込み，指定した領域の輝度値を反転させるプログラム

#(20)カラー画像を読み込み，指定した領域でトリミングするプログラム。


#(21)カラー画像を読み込み，3×3 の領域で平均値によりプーリングするプログラムを作成せよ。

#(22)カラー画像を読み込み，3×3 の領域で最大値によりプーリングするプログラムを作成せよ。

#(23)指定した 2 枚のカラー画像を読み込み，差分画像を作成するプログラム(類似画像を利用)
