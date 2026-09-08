"""
[그리디 알고리즘 - 거스름돈]

문제 설명:
- 그리디알고리즘으로 거스름돈을 계산.
- 가장 큰 단위의 동전부터 사용하여 최소 개수로 거슬러줍니다.
- 매 순간 최선의 선택(가장 큰 동전)을 합니다.

입력:
- change: 거슬러줄 금액
- coins: 사용 가능한 동전 종류 (예: [500, 100, 50, 10])

출력:
- 필요한 동전의 개수
- 각 동전의 사용 개수

예제:
입력: change = 1260, coins = [500, 100, 50, 10]
출력:
500원: 2개
100원: 2개
50원: 1개
10원: 1개
총 6개

힌트:
- 1. 큰 동전부터 사용
- 2. 현재 동전으로 최대한 거슬러주기
- 3. 나머지 금액으로 다음 동전 사용
"""

# 그리디 알고리즘은 항상 local optinum(액면가가 가장 큰 동전)을 선택한다.
# 그래서 global optimum(최소 개수의 동전) 을 보장하지는 않는다.
# 하지만 동전 시스템에서 큰 단위가 작은 단위의 배수가 되는 특별한 구조(Canonical Coin System)에서는
# 항상 최소 개수의 정답을 찾아낸다.

def make_change_greedy(change, coins):  # change: 거슬러줄 금액, coins: 동전 종류 리스트(내림차순)
    
    result = {}         # {동전 가치: 사용 개수}
    total_coins = 0     # 거슬러준 동전의 총 개수
    
    # 각 동전에 대해 반복
    # 현재 동전으로 거슬러줄 수 있는 개수 계산    
    # 개수가 0보다 크면 결과에 추가
    for coin in coins:
        if coin <= change:
            num = change // coin
            change = change % coin
            if num > 0:
                result[coin] = num
                total_coins += num
            if change == 0:    
                break
    return total_coins, result

# 1. 큰 동전부터 차례대로 순회한다
#   coins 리스트가 내림차순으로 정렬되어 있으므로, 바로 for문 돌림
#   반복문으로 가장 큰 동전부터 1개씩 꺼내서, 남은 거스름돈과 비교
# 2. 현재 동전으로 거슬러줄 수 있는 개수 구하기
#   (소수점이 남지 않도록) 나눗셈의 몫 연산을 활용 (현재 동전의 사용 개수 구해짐)
# 3. 남은 금액 갱신
#   방금 사용한 동전들의 총액(동전 가치 x 개수)을 전체 남은 거스름돈에서 뺴거나, 나머지 연산을 해서,
#   다음 동전에게 넘겨줄 잔돈을 갱신
# 4. 결과 기록 및 누적
#   만약 계산된 동전의 개수가 0보다 크면, 결과 딕셔너리에 [동전 가치: 사용 개수] 형태로 기록
#   전체 동전 개수 누적 변수에도 방금 사용한 동전 개수를 더해줌
#   거스름돈이 0원이 되면, 더 이상 계산할 필요가 없으므로, 반복문을 탈출(break)하는 최적화 로직



# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    change1 = 1260
    coins1 = [500, 100, 50, 10]
    total, details = make_change_greedy(change1, coins1)    # details 의 타입은 dictionary 이다.
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change1}원")
    for coin, count in details.items():                     # dictionary 순회, Tuple Unpacking
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()
    
    # 테스트 케이스 2
    change2 = 4570
    coins2 = [500, 100, 50, 10]
    total, details = make_change_greedy(change2, coins2)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change2}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")
    print()
    
    # 테스트 케이스 3
    change3 = 1000
    coins3 = [500, 100, 50, 10]
    total, details = make_change_greedy(change3, coins3)
    
    print("=== 거스름돈 계산 ===")
    print(f"거슬러줄 금액: {change3}원")
    for coin, count in details.items():
        print(f"{coin}원: {count}개")
    print(f"총 {total}개")


