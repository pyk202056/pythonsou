from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score, train_test_split

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    plt = None

# [RandomForest 문제]
# Red Wine Quality 데이터를 사용해 와인의 품질 점수(0~10)를 분류한다.
# 데이터 파일: winequality-red.csv

data_path = Path(__file__).resolve().parent / "winequality-red.csv"
df = pd.read_csv(data_path)

print(df.head(2))
print(df.info())
print(df.isnull().any())

# 독립변수(x), 종속변수(y)
x = df.drop("quality", axis=1)
y = df["quality"]

train_x, test_x, train_y, test_y = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)

# 모델 생성
model = RandomForestClassifier(
    criterion="gini",
    n_estimators=500,
    random_state=1,
    class_weight="balanced",
)
model.fit(train_x, train_y)
pred = model.predict(test_x)

print("예측값:", pred[:5])
print("실제값:", np.array(test_y[:5]))
print("맞춘 개수:", int(np.sum(test_y == pred)))
print("전체 대비 일치 비율:", np.sum(test_y == pred) / len(test_y))
print("분류 정확도:", accuracy_score(test_y, pred))
print("classification_report:\n", classification_report(test_y, pred, zero_division=0))

# 교차 검증
cross_vali = cross_val_score(model, x, y, cv=5)
print(cross_vali)
print("교차 검증 평균 정확도:", np.round(np.mean(cross_vali), 5))

print("중요 변수 확인 -----")
print("특성 중요도:", model.feature_importances_)

# 중요도 시각화
if plt is not None:
    n_features = x.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align="center")
    plt.xlabel("Feature Importance Score")
    plt.ylabel("Features")
    plt.yticks(np.arange(n_features), x.columns)
    plt.ylim(-1, n_features)
    plt.tight_layout()
    plt.show()
    plt.close()
else:
    print("matplotlib이 없어 중요도 그래프는 건너뜁니다.")

# 새로운 와인 데이터 예측
new_wine = [[7.5, 0.5, 0.3, 2.0, 0.08, 15.0, 50.0, 0.997, 3.3, 0.6, 10.5]]
new_pred = model.predict(new_wine)
print(f"새 와인 샘플의 예측 품질 등급: {new_pred[0]}")
