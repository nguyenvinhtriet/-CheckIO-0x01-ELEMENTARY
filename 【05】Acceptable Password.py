# =====================================
# --*-- coding: utf-8 --*--
# @Author  : trietnv
# @Date    : 2020-04-23
# @CSDN    : 
# @FileName: 【05】Acceptable Password.py
# =====================================
def is_acceptable_password(password: str) -> bool:
    # your code here
    if(len(password)>6):
      return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
