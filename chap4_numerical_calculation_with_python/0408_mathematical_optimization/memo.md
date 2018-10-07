### TypeError: Image data cannot be converted to float
URL: https://stackoverflow.com/questions/32302180/typeerror-image-data-can-not-convert-to-float
>This question comes up first in the Google search for this type error,
>but does not have a general answer about the cause of the error.
>The poster's unique problem was the use of an inappropriate object type
>as the main argument for plt.imshow().
>A more general answer is that plt.imshow() wants an array of floats
>and if you don't specify a float, numpy, pandas,
>or whatever else, might infer a different data type somewhere along the line. 
>You can avoid this by specifying a float for the dtype argument is the constructor of the object.

dtype of return value of ufunc is changed, 
so z must be casted to np.float64.

### ValueError: could not broadcast input array from shape (2,1) into shape (2)
お察しの通り、以下の部分が問題でしょうね。
グレースケールの場合、1ピクセルにあるデータは１つとなってますが、RGBの場合１ピクセルには3つのデータが存在します。

```python
# 例）3*3pxの画像データを想定した時のデータはこの様なイメージです。

# グレーの場合
[[2,5,6],
 [5,4,2],
 ......
 [8,4,1]]

# RGBの場合
[[[2,5,4],[5,6,7],[8,9,2],
 [[5,4,2],[6,8,4],[1,2,4]],
 ......
 [[5,1,4],[2,6,8],[4,1,5]]]
```

画像データはグレースケール画像ではなくRGB画像です。
もしかしたらそこがいけないのかもしれません。。。