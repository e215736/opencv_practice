"""
reference:
https://dsf-kotaro.hatenablog.com/entry/2022/06/07/120000
"""

import cv2
import urllib.request as req

#フリーの画像を検索して、ファイルリンクをコピー
url = "https://jp.static.photo-ac.com/assets/img/ai_page/ai_model_512_01.png"
#download the image from the specified URL 
# and save it as "face_test.png" in the current directory.
req.urlretrieve(url, "face_test.png")

#reads the image file "face_test.png" using the 
# imread function 
# from the OpenCV library and 
# assigns(allocate)  the image data to the variable img.
img = cv2.imread("face_test.png")
print(img)

#3次元データ確認
print(img.shape)
#return:(512, 512, 3)
#これは高さ512画素，幅512画素，RGBの3つで表されている．


#OpenCVはmatplotlibと互換性がある
import matplotlib.pyplot as plt

#軸表示消した．別にいらん
plt.axis("off")

#matplotlib.pyplotのimshow()関数で画像を表示
#cv2.COLOR_BGR2RGB):BGRからRGBに変換
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()


#=========画像の保存=============
#imwrite関数で、保存後のファイル名とファイルデータの入った変数を指定して画像を保存
cv2.imwrite("output.png", img)


#=========画像のリサイズ=============

#元画像のサイズは512×512でしたので、それをよこ600×たて300
#元々の画像のアスペクト比（縦横比）と異なるため変になる

#アスペクト比が異なる場合は、画像を変更後のアスペクト比で切り取ってリサイズを行いましょう。??

img2 = cv2.resize(img, (600, 300))
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.show()

#=========画像の切り取り=============

#元画像から顔の部分を中心に切りとる
#imgのデータをスライスを使ってデータを取り出す

#今回の例では，画像の左上の座標が（０，０）、右下の座標が（512、521）

#水平方向のピクセルを0から400まで、垂直方向のピクセルを50から450まで切り取る操作
img3 = img[0:400,50:450]

#ピクセル数400*400にリサイズ
img3 = cv2.resize(img3, (400,400))

plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
plt.show()
