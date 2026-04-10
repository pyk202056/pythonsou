import pandas as pd
import numpy as np
from sklearn.datasets import fetch_openml   # OpenML에서 데이터셋 불러오기
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold  # 데이터 분리 및 튜닝
from sklearn.pipeline import Pipeline   # 전처리 + 모델을 하나로 묶기
from sklearn.compose import ColumnTransformer   # 컬럼별 전처리 다르게 적용
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer   # 결측치 처리
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

# Adult Income 데이터셋 불러오기
adult = fetch_openml(name='adult', version=2, as_frame=True)   
df = adult.frame   # pandas DataFrame 형태로 변환

print(df.head(2))
print(df.shape)

# target 변환 : 연봉 >50K → 1, 아니면 0으로 변환
df['class'] = df['class'].apply(lambda x: 1 if '>50K' in x else 0)   

X = df.drop('class', axis=1)   # feature
y = df['class']                # label
print(X.info())

# 컬럼 분리 : 숫자형, 범주형
num_cols = X.select_dtypes(include=['int64', 'float64']).columns   # 숫자형 컬럼 선택
cat_cols = X.select_dtypes(include=['object', 'category']).columns # 범주형 컬럼 선택

# 전처리 파이프라인 (숫자형)
num_pipeline = Pipeline([  # Pipeline = 전처리 + 모델을 한 번에 연결해 실행(한 줄로 처리 가능)
    ('imputer', SimpleImputer(strategy='median')),   # 결측치 → 중앙값으로 채움
    ('scaler', StandardScaler())   # 표준화 (평균0, 분산1)
])

# 전처리 파이프라인 (범주형)
cat_pipeline = Pipeline([
    # SimpleImputer : 누락된 값을 특정 기준으로 채우는 전처리 클래스
    ('imputer', SimpleImputer(strategy='most_frequent')), # 결측치 → 최빈값으로 채움
    ('onehot', OneHotEncoder(handle_unknown='ignore'))    # 범주형 → One-Hot 인코딩
])

# 컬럼별 전처리 결합
# ColumnTransformer:컬럼별로 다른 전처리를 적용하는 도구
# 숫자 → 스케일링, 문자 → 인코딩 : 각각 다르게 처리해야 함
preprocess = ColumnTransformer([
    ('num', num_pipeline, num_cols),   # 숫자형 컬럼에 num_pipeline 적용
    ('cat', cat_pipeline, cat_cols)    # 범주형 컬럼에 cat_pipeline 적용
])

# 전체 파이프라인 (전처리 + 모델)
pipeline = Pipeline([
    ('prep', preprocess),   # 전처리 단계
    ('model', RandomForestClassifier(random_state=12))   # 모델 단계
])

# train/test 분리
train_x, test_x, train_y, test_y = train_test_split(
    X, y, test_size=0.3, random_state=12, stratify=y   # stratify로 클래스 비율 유지
)

# 하이퍼파라미터 튜닝 범위 설정
param_grid = {
    'model__n_estimators': [100, 200],   # 트리 개수
    'model__max_depth': [5, 10, None],   # 트리 깊이
    'model__class_weight': [None, 'balanced']   # 클래스 불균형 보정
}

# 교차검증 설정
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=12)   # 5겹 CV, 클래스 비율 유지

# GridSearchCV 설정
grid = GridSearchCV(
    pipeline,      # 전체 파이프라인 사용
    param_grid,    # 탐색할 파라미터
    cv=cv,         # 교차검증 방식
    scoring='roc_auc',   # 평가 기준 (ROC-AUC)
    n_jobs=-1      # 모든 CPU 사용
)

# 학습
grid.fit(train_x, train_y)   # 최적 파라미터 탐색 + 학습 수행
print("최적 파라미터:", grid.best_params_)   # 최적 파라미터 출력

# 예측
pred = grid.predict(test_x)   # 테스트 데이터 클래스 예측
proba = grid.predict_proba(test_x)[:, 1]   # 클래스 1에 대한 확률값

# 평가
print("\n정확도:", accuracy_score(test_y, pred))   # 전체 정확도
print("\nROC-AUC:", roc_auc_score(test_y, proba))  # ROC-AUC 점수
print("\nClassification Report:\n", classification_report(test_y, pred))  # 정밀도, 재현율, f1-score 출력