# Airflow Platform Sample for AKS

이 샘플은 AKS에서 Airflow를 운영하기 위한 표준 디렉토리 구조 예시이다

포함 범위
- DAG 공통 설정
- DAG 템플릿
- common_lib 공통 모듈
- plugin operator 예시
- Helm values 예시
- Dynamic DAG 설정 예시
- 테스트 예시
- Dockerfile 및 requirements 예시


sample-app
├── src
│   ├── main.py
│   └── utils.py
├── common
│   └── db
│       ├── postgres_config.py
│       ├── postgres_tasks.py
│       └── postgres_helper.py
├── db
│   └── postgresql_template.py
├── requirements.txt
├── README.md
└── .gitignore