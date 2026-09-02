"""
[문자열 - 회문(Palindrome) 판별]

문제 설명:
- 주어진 문자열이 회문(앞에서 읽으나 뒤에서 읽으나 같은 문자열)인지 판별합니다.
- 대소문자를 구분하지 않고, 공백과 특수문자는 무시합니다.

입력:
- s: 판별할 문자열

출력:
- True: 회문인 경우
- False: 회문이 아닌 경우

예제:
입력: "A man, a plan, a canal: Panama"
출력: True

입력: "race a car"
출력: False

힌트:
- 알파벳과 숫자만 남기고 소문자로 변환하세요
- 문자열을 뒤집어서 비교하거나, 양 끝에서 시작해 중앙으로 이동하며 비교하세요
"""


import re

def is_palindrome(s: str) -> bool:

    """
    파이써닉 방식:
    정규식으로 alpha/num 만 남기고 소문자로 바꾼 뒤,
    슬라이싱을 이용해 문자열을 뒤집어서 원본과 비교한다.
    """

    # 1. alpha/num 만 골라내서 소문자로 변환
    cleaned = ''.join(char.lower() for char in s if char.isalnum())

    # 2. 뒤집은 문자열과 비교
    return cleaned == cleaned[::-1]


# 테스트 케이스
if __name__ = "__main__":
    # 테스트 케이스 1
    test1 = "A man, a plan, a canal: Panama"
    result1 = is_palindrome(test1)
    print(f"입력: \"{test1}\"")
    print(f"회문 여부: {result1}")
    print()

    # 테스트 케이스 2
    test2 = "race a car"
    result2 = is_palindrome(test2)
    print(f"입력: \"{test2}\"")
    print(f"회문 여부: {result2}")
    print()

    # 테스트 케이스 3
    test3 = "Was it a car or a cat I saw?"
    result3 = is_palindrome(test3)
    print(f"입력: \"{test3}\"")
    print(f"회문 여부: {result3}")
    print()

    # 테스트 케이스 4
    test4 = "Madam"
    result4 = is_palindrome(test4)
    print(f"입력: \"{test4}\"")
    print(f"회문 여부: {result4}")


"""
def is_palindrome(s):
    
    # TODO: 알파벳과 숫자만 남기고 소문자로 변환하세요
    # 힌트: isalnum() 메서드와 lower() 메서드 사용
    
    left = 0
    right = len(s) - 1

    while left < right:
        # 1. 왼쪽 포인터가 alpha/num 이 아니면, 오른쪽으로 이동하며 건너뜀
        while left < right and not s[left].isalnum():
            left += 1

        # 2 . 오른쪽 포인터가 alpha/num 이 아니면, 왼쪽으로 이동하며 건너뜀
        while left < right and not s[right].isalnum():
            right -= 1

        # 3.
        if s[left].lower() != s[right].lower():
            return False
        
        # 4. 일치하므로 안쪽으로 1칸씩 좁혀나감
        left += 1
        right -= 1

    return True
    
    # TODO: 정제된 문자열이 회문인지 확인하세요
    # 방법1: 문자열을 뒤집어서 비교 ([::-1] 사용)
    # 방법2: 양 끝 인덱스를 이용한 투 포인터 방식
    pass
    
    #return False

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "A man, a plan, a canal: Panama"
    result1 = is_palindrome(test1)
    print(f"입력: \"{test1}\"")
    print(f"회문 여부: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "race a car"
    result2 = is_palindrome(test2)
    print(f"입력: \"{test2}\"")
    print(f"회문 여부: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "Was it a car or a cat I saw?"
    result3 = is_palindrome(test3)
    print(f"입력: \"{test3}\"")
    print(f"회문 여부: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "Madam"
    result4 = is_palindrome(test4)
    print(f"입력: \"{test4}\"")
    print(f"회문 여부: {result4}")


"""
