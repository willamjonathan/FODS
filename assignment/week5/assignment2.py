# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14OE5cy9p1ZEiL0I-yRUpwTuSpWlyRgRO

ASSIGNMENT 2 - WILLIAM JONATHAN M
L3AC
2502045683
"""



import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm,datasets
from sklearn.svm import  SVC
import numpy as np
from sklearn.metrics import accuracy_score

df = pd.read_csv('aftercleaning.csv')
df.info()

#143745 - mean
df['label']=np.where(df['Reported number of people receiving ART']>143744,'good','bad')
df

#cutting the data only up to 100
X=df.iloc[0:76,[1,7]]
y=df.loc[0:75,'label']

#if c is inreased more accurate; c=1 accuracy 1
clf = svm.SVC(kernel='rbf', gamma=0.08, C=1)

#train the model
clf.fit(X, y)

#just use the same data to predict for now
y_pred=clf.predict(X)


print(accuracy_score(y, y_pred))

#PLOTTING


plt.scatter(df['Estimated number of people living with HIV_median'][df['label']=='good'],
            df['Reported number of people receiving ART'][df['label']=='good'],color='green', marker='*',label ="Good")
plt.scatter(df['Estimated number of people living with HIV_median'][df['label']=='bad'],
            df['Reported number of people receiving ART'][df['label']=='bad'],color='red', marker='.',label ="Bad")

plt.xlabel('Estimated number of people living with HIV_median')
plt.ylabel('Reported number of people receiving ART')
#location legend
plt.legend(loc='best')
plt.show()


##########################################################################
# #PART 2 - for this part i failed in running the code, eventho i've tried so many attempts 

# # # model_linear_kernal = SVC(kernel='linear')
# # # model_linear_kernal.fit(x_train, y_train)

# # def plot_contours(ax, clf, xx, yy, **params):
# #     Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
# #     Z = Z.reshape(xx.shape)
# #     out = ax.contourf(xx, yy, Z, **params)
# #     return out

# # def make_meshgrid(x, y, h=.02):
# #     x_min, x_max = x.min() - 1, x.max() + 1
# #     y_min, y_max = y.min() - 1, y.max() + 1
# #     xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
# #     return xx, yy


# # fig, ax = plt.subplots()
# # # title for the plots
# # title = ('SVC HIV ')
# # # Set-up grid for plotting.
# # X0, X1 = X.iloc[:, 0], X.iloc[:, 1]
# # xx, yy = make_meshgrid(X0, X1)

# # plot_contours(ax, svm, xx, yy, cmap=plt.cm.YlGn, alpha=0.8)
# # ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
# # ax.set_xlabel('Estimated number of people living with HIV_median')
# # ax.set_ylabel('Reported number of people receiving ART')
# # ax.set_xticks(())
# # ax.set_yticks(())
# # ax.set_title(title)
# # plt.show()
# def make_meshgrid(x, y, h=.02):
#     x_min, x_max = x.min() - 1, x.max() + 1
#     y_min, y_max = y.min() - 1, y.max() + 1
#     xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
#     return xx, yy


# def plot_contours(ax, clf, xx, yy, **params):
#     Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
#     Z = Z.reshape(xx.shape)
#     out = ax.contourf(xx, yy, Z, **params)
#     return out


# fig, ax = plt.subplots()
# # title for the plots
# title = 'HIV median and ART classification'
# # Set-up grid for plotting.
# #X0, X1 = X.iloc[:, df['Estimated number of people living with HIV_median']], X.iloc[:, df['Reported number of people receiving ART']]
# # X0=df['Reported number of people receiving ART']
# # X1=df['Country']
# xx, yy = make_meshgrid(X0, X1)

# plot_contours(ax, svm, xx, yy, cmap=plt.cm.YlGn, alpha=0.8)
# ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=50, alpha=0.7 )
# ax.set_xlabel('Estimated number of people living with HIV_median')
# ax.set_ylabel('Reported number of people receiving ART')
# ax.set_xticks(())
# ax.set_yticks(())
# ax.set_title(title)
# plt.show()

