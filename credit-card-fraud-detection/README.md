# Credit Card Fraud Detection

ML 프로젝트: 신용카드 사기 거래 탐지 (Binary Classification)

## 프로젝트 개요

이 프로젝트는 신용카드 거래 데이터를 분석하여 사기 거래를 탐지하는 이진 분류 모델을 개발합니다.

**주요 특징:**
- 불균형 데이터셋 다루기 (사기 거래는 전체의 약 0.17%)
- Logistic Regression을 활용한 분류
- Feature Engineering 및 EDA
- 모델 평가: Precision, Recall, F1-Score, ROC-AUC

## 데이터셋

**출처:** [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

**데이터 다운로드 방법:**

### 방법 1: Kaggle CLI 사용 (추천)

1. Kaggle 계정 생성 및 API 토큰 발급
   - [Kaggle](https://www.kaggle.com) 로그인
   - Account → API → Create New API Token
   - `kaggle.json` 파일 다운로드

2. Kaggle CLI 설치 및 인증
```bash
pip install kaggle
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

3. 데이터셋 다운로드
```bash
cd credit-card-fraud-detection/data
kaggle datasets download -d mlg-ulb/creditcardfraud
unzip creditcardfraud.zip
```

### 방법 2: 수동 다운로드

1. [데이터셋 페이지](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) 방문
2. "Download" 버튼 클릭
3. `creditcard.csv` 파일을 `data/` 폴더에 저장

## 데이터 설명

- **Time**: 첫 거래 이후 경과 시간(초)
- **V1-V28**: PCA를 통해 변환된 익명화된 특성들
- **Amount**: 거래 금액
- **Class**: 사기 여부 (1 = 사기, 0 = 정상)

## 프로젝트 구조

```
credit-card-fraud-detection/
├── README.md
├── data/
│   └── creditcard.csv (다운로드 필요)
├── notebooks/
│   └── 01-eda-and-baseline.ipynb
└── models/
    └── (학습된 모델 저장)
```

## 기술 스택

- Python 3.13
- NumPy, Pandas
- Scikit-learn
- Matplotlib, Seaborn

## 학습 목표

1. **불균형 데이터 처리**
   - Class Imbalance 문제 이해
   - SMOTE, Undersampling 등의 기법 적용

2. **적절한 평가 지표 선택**
   - Accuracy의 한계 이해
   - Precision, Recall, F1-Score 활용
   - ROC Curve와 AUC

3. **모델 해석**
   - Feature Importance 분석
   - Threshold 조정

## 참고 자료

- [ML Zoomcamp Week 3: Classification](https://github.com/DataTalksClub/machine-learning-zoomcamp)
- [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
