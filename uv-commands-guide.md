# uv 가상환경 명령어 가이드

uv는 Rust로 작성된 매우 빠른 Python 패키지 및 프로젝트 관리자입니다. 이 문서는 uv의 주요 가상환경 관련 명령어들을 정리한 것입니다.

## 목차
1. [가상환경 생성](#가상환경-생성)
2. [가상환경 활성화/비활성화](#가상환경-활성화비활성화)
3. [Python 버전 관리](#python-버전-관리)
4. [환경 탐색 및 관리](#환경-탐색-및-관리)
5. [기타 유용한 명령어](#기타-유용한-명령어)

## 가상환경 생성

### 기본 가상환경 생성
```bash
uv venv
```
현재 디렉토리에 `.venv`라는 이름의 가상환경을 생성합니다.

### 사용자 정의 이름으로 가상환경 생성
```bash
uv venv my-env
```
`my-env`라는 이름의 가상환경을 생성합니다.

### 특정 Python 버전으로 가상환경 생성
```bash
uv venv --python 3.11
```
또는
```bash
uv venv --python 3.12.0
```
지정한 Python 버전으로 가상환경을 생성합니다.

## 가상환경 활성화/비활성화

### 활성화

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (cmd):**
```cmd
.venv\Scripts\activate.bat
```

**다른 쉘 환경:**
- Fish: `source .venv/bin/activate.fish`
- Csh/tcsh: `source .venv/bin/activate.csh`
- Nushell: `source .venv/bin/activate.nu`

### 비활성화
```bash
deactivate
```

## Python 버전 관리

### Python 버전 목록 확인
```bash
uv python list
```
설치 가능한 Python 버전 목록을 표시합니다.

### Python 버전 설치
```bash
# 단일 버전 설치
uv python install 3.11

# 여러 버전 동시 설치
uv python install 3.10 3.11 3.12
```

### 설치된 Python 버전 찾기
```bash
uv python find
```
시스템에서 사용 가능한 Python 인터프리터를 찾습니다.

### Python 버전 고정
```bash
uv python pin 3.11
```
현재 디렉토리에서 사용할 Python 버전을 고정합니다. `.python-version` 파일이 생성됩니다.

### Python 설치 디렉토리 확인
```bash
uv python dir
```
Python 설치 디렉토리 경로를 표시합니다.

### Python 버전 제거
```bash
uv python uninstall 3.10
```
지정한 Python 버전을 제거합니다.

### Python 버전 업그레이드
```bash
uv python upgrade
```
설치된 Python 버전을 최신으로 업그레이드합니다.

## 환경 탐색 및 관리

### 환경 탐색 우선순위
uv는 다음 순서로 가상환경을 탐색합니다:
1. 활성화된 가상환경 (`VIRTUAL_ENV` 환경변수)
2. 활성화된 Conda 환경 (`CONDA_PREFIX` 환경변수)
3. 현재 디렉토리 또는 상위 디렉토리의 `.venv`

### 특정 Python 버전으로 스크립트 실행
```bash
uv run --python 3.11 script.py
```

### 시스템 전역 설치 (가상환경 없이)
```bash
uv pip install --system package-name
```
⚠️ 주의: 가상환경 사용을 권장합니다.

## 기타 유용한 명령어

### 패키지 설치
```bash
# 가상환경 내에서
uv pip install package-name

# requirements.txt 파일로부터 설치
uv pip install -r requirements.txt
```

### 설치된 패키지 목록 확인
```bash
uv pip list
```

### 패키지 업그레이드
```bash
uv pip install --upgrade package-name
```

### 패키지 제거
```bash
uv pip uninstall package-name
```

### 프로젝트 환경 동기화
```bash
uv sync
```
프로젝트의 의존성을 동기화합니다.

## 추가 팁

1. **가상환경 자동 생성**: uv는 가상환경이 없을 때 자동으로 생성을 제안합니다.

2. **빠른 성능**: uv는 Rust로 작성되어 pip보다 10-100배 빠른 성능을 제공합니다.

3. **프로젝트별 Python 버전**: `.python-version` 파일을 사용하여 프로젝트마다 다른 Python 버전을 사용할 수 있습니다.

4. **호환성**: uv는 pip와 호환되는 인터페이스를 제공하므로 기존 워크플로우를 쉽게 전환할 수 있습니다.

## 참고 자료
- [uv 공식 문서](https://docs.astral.sh/uv/)
- [uv GitHub 저장소](https://github.com/astral-sh/uv)