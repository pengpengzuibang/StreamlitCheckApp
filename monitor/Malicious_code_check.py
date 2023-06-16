import subprocess

def detect_malicious_code(function_code):
    # 使用静态代码分析工具Bandit检测恶意代码
    result = subprocess.run(['bandit', '-r', '-ll', '-ii', '-x', 'tests', '-n', '5', '-c', 'bandit.yml'], input=function_code, capture_output=True, text=True)

    if result.returncode == 0:
        print("函数没有恶意代码")
    else:
        print("函数包含恶意代码")
        print(result.stdout)

# 示例函数
def my_function():
    code = """
    # 这是一个恶意代码示例
    import os
    os.system("rm -rf /")
    """

    detect_malicious_code(code)

# 测试函数
my_function()
