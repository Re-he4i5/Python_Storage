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
from PIL import Image
import numpy as np

img = Image.open("image.jpg")
w,h = img.size

img_resize2 = img.resize(((w*2),(h*2)))
img_resize_05 = img.resize(((w // 2),(h // 2)))

img_resize2.save("save_1.jpg")
img_resize_05.save("save_1.jpg")
#(6)アフィン変換により画像を拡大・縮小するプログラム

def scale_matrix(sx,sy):
    M = np.array([[sx,0 ,0],
                  [0 ,sy,0]])
    return M

img = Image.read("image.jpg")
w,h = img.shape[:2]

M2 = scale_matrix(sx= 2.0,sy = 2.0)
M05 = scale_matrix(sx= 0.5,sy = 0.5)

dst2 =cv2.warpAffine(img,M2,dsize = (w*2, h*2))
dst05 =cv2.warpAffine(img,M05,dsize = (w*2, h*2))

cv2.imshow("twice",dst2)
cv2.imshow("half",dst05)

cv2.imwrite("image.jpg",dst2)

cv2.imwrite("image.jpg",dst05)

#(7)アフィン変換により，画像を平行移動するプログラム。
img = cv2.imread("cat.jpg")
h,w = img.shape[:2]
dx,dy = 500,500

afn_mat = np.float32([[1,0,dx],
                      [0,1,dy]])
img_afn = cv2.warpAffine(img,afn_mat,(w,h))

cv2.imshow("trans",img_afn)

#(8)アフィン変換により，画像を回転するプログラム
img = cv2.imread("cat.jpg")
h,w = img.shape[:2]

rot_mat = cv2.getRotationMatrix2D((w/2,h/2),40,1)
img_afn =cv2.warpAffine(img,rot_mat,(w,h))
cv2.imshow("trans",img_afn)

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
