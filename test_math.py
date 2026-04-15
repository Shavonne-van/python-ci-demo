# test_math.py
from math_utils import add, multiply

def test_add_positive():
    """测试正数加法"""
    assert add(2, 3) == 5

def test_add_negative():
    """测试负数加法"""
    assert add(-1, 1) == 0

# 故意写一个失败的测试，用于作业要求的「失败→修复」演示
def test_multiply_fail_demo():
    """故意制造失败的乘法测试（初始错误版）"""
    assert multiply(2, 3) == 7  # 预期错误值7，实际正确结果为6