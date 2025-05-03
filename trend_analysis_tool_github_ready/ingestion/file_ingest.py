import time

def load_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return [{
        "source": "file",
        "timestamp": time.time(),
        "content": line.strip(),
        "keyword": "uploaded"
    } for line in lines if line.strip()]
