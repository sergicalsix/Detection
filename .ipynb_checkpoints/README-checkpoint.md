## 概要
マスク着用の有無を検出するためのプログラム

## 仕様
opencvを使用

口の検出に関して偽陽性(過剰に検出してしまう)が多いので、口候補の領域の内、もっとも下にある領域を口と仮定(口が下にあると仮定)

![過剰に検出](no_mask_incorrect.png) 

誤った例
![正しい検出](no_mask_correct.png) 

## データ
- face 

https://github.com/opencv/opencv/tree/master/data/haarcascades

- mouth 

https://github.com/opencv/opencv_contrib/blob/1311b057475664b6af118fd1a405888bad4fd839/modules/face/data/cascades


