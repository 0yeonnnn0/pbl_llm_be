# Help Coding Test!

## How to Start

### 1. environment settings

<br>

**1.1 make virtual environment**

```
python -m venv .venv
```

<br>

**1.2 activate virtual environment**

- Windows

```
.venv\Scripts\activate
```

- MacOS/Linux

```
source .venv/bin/activate
```

<br>

**1.3 install dependencies**

```
pip install -r requirements.txt
```

### 2. start code

```
uvicorn app.main:app --reload
```
