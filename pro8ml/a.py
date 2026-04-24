# wine dataset으로 다항 분류
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = load_wine()
x = data.data
y = data.target  # 3개 클래스 (0,1,2)
print(x[:2])
print(y[:2])
print(data.feature_names)
print("데이터 shape:", x.shape)
print("클래스:", np.unique(y))

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42, stratify=y
)

# 스케일링 (MLP 필수)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# 모델 생성
model = MLPClassifier(
    hidden_layer_sizes=(50, 30),  # 은닉층 2개
    activation='relu',
    solver='adam',
    learning_rate_init=0.001,
    max_iter=10,
    random_state=42
)

model.fit(x_train_scaled, y_train)
pred = model.predict(x_test_scaled)

print("\nAccuracy:", accuracy_score(y_test, pred))
print("\nClassification Report:\n", classification_report(y_test, pred))

# Confusion Matrix 시각화
cm = confusion_matrix(y_test, pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# 학습 Loss Curve 시각화
plt.plot(model.loss_curve_)
plt.title("Training Loss Curve")
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.show()