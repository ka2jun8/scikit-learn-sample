from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def train(vectors, labels):
    #トレーニング・テストデータの設定
    train_data = vectors

    x_train, x_test, y_train, y_test = train_test_split(train_data, labels, test_size=0.4, random_state=1)

    #データの標準化
    sc = StandardScaler()
    sc.fit(x_train)
    x_train_std = sc.transform(x_train)
    x_test_std = sc.transform(x_test)

    #学習モデルの作成
    clf = SVC(C = 1, kernel = 'rbf')
    clf.fit(x_train_std, y_train)

    score = clf.score(x_test_std, y_test)
    print("score: {:.3g}".format(score))

    return clf
