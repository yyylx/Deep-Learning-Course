import tensorflow as tf
import matplotlib. pyplot as plt
import numpy as np
boston_housing = tf.keras.datasets.boston_housing
(train_x, train_y), (_,_) = boston_housing.load_data(test_split=0)

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
titles = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE",
          "DIS","RAD","TAX","PTRATIO", "B-1000", "LSTAT", "MEDV"]
plt . figure(figsize=(12,12))
for i in range(13):
    plt.subplot(4, 4, (i + 1))
    plt.scatter(train_x[:, i], train_y)
    plt.xlabel(titles[i])
    plt.ylabel("Price($1000's)")
    plt.title(str(i + 1) + "." + titles[i] + " - Price")
plt. tight_layout()
plt. suptitle("各属性与房价的关系", x=0.5, y=1.02, fontsize=20)
plt.show()
for j in range(13):
    print(j+1,"--",titles[j])
index=int(input("请选择属性:"))
plt . figure(figsize=(5,5))
plt.scatter(train_x[:,5], train_y)
plt.xlabel(titles[index-1])
plt.ylabel("Price($1000's)")
plt.title(str(index-1) + "." + titles[index-1] + " - Price")
plt.show()