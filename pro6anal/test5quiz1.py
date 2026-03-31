import pandas as pd
import scipy.stats as stats

# 데이터 로드
df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/cleanDescriptive.csv")

# level, pass 열에 NA 행 제외
df_clean = df.dropna(subset=['level', 'pass'])
print(df_clean.head())
print(df_clean['level'].unique())  # [1. 2. 3.]
print(df_clean['pass'].unique())   # [2. 1.]
print()
ctab = pd.crosstab(index=df_clean['level'], columns=df_clean['pass'])
print(ctab)

chi2, p, dof, expected = stats.chi2_contingency(ctab)

print(f"\n카이제곱: {chi2}")    # 카이제곱: 2.7669512025
print(f"p-value: {p}")         # p-value: 0.2507056840

if p < 0.05:
    print(f"판정: p-value({p}) < 0.05 이므로 귀무가설을 기각 => 통계적으로 유의미")
else:
    print(f"판정: p-value({p}) >= 0.05 이므로 귀무가설을 채택 => 통계적 관련 없음")