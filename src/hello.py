# 示例脚本：打印一句问候并显示当前时间
from datetime import datetime

def greet(name: str = "世界") -> str:
    return f"你好，{name}！现在是 {datetime.now():%Y-%m-%d %H:%M:%S}"

if __name__ == "__main__":
    print(greet())