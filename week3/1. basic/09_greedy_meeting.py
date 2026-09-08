"""
[그리디 - 회의실 배정]

문제 설명:
- 하나의 회의실에 여러 회의를 배정합니다.
- 각 회의는 시작 시간과 종료 시간이 있습니다.
- 최대한 많은 회의를 배정하려고 합니다.

입력:
- meetings: [(시작, 종료), ...] 회의 리스트

출력:
- 배정된 회의 개수

예제:
입력: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
출력: 4개
선택: [(1, 4), (5, 7), (8, 11), (12, 14)]

힌트:
- 종료 시간이 빠른 회의부터 선택!
- 이전 회의가 끝난 후에 시작하는 회의만 선택
"""


# 회의실 (구간) 일정 편성 문제
# 단일 자원(회의실) 에서 중복되지 않고 진행될 수 있는 활동(회의) 의 수를 최대화

# 이 문제에서 그리디 알고리즘이 효과적인 이유:
#   한 회의실에 최대한 많은 회의를 채우려면, 각 단계에서 향후 회의에 사용 가능 공간을 최대한 남겨두는 국소 최적 선택을 해야함

# 함정 (다른 선택이 실패하는 이유)
#   - 가장 짧은 회의를 먼저 선택하면, 짧은 회의가 하루 중 정오까지 이어져, 그 시간에 들어갈 수 있었던 다른 두 회의가 막힐 수 있음#   - 가장 이른 시작 시간을 먼저 선택하면, 회의가 일찍 시작되어 하루 종일 이어지면서, 다른 모든 일정을 막을 수 있음

# 전략 (가장 이른 종료 시간)
#   모든 회의를 종료 시간 순으로 정렬 (오름차순)
# 


# 모든 (시작, 종료) 구간을 검토하여, 서로 겹치지 않는 회의를, 최대한 많이 선정
# 탐욕: 항상 가장 빨리 끝나는 회의를 선택하라
#  - 선형적이고 후회 없는 진행 방식

def select_meetings(meetings):  # meetings: [(start_time, end_time)]
                                    # start_time: 회의가 시작되고 회의실이 점유되는 시간
                                    # end_time: 회의가 끝나고   회의실이 다음 예약을 위해 비워지는 시간
 
    # meetings 가  없으면 0 반환
    if not meetings:
        return 0, []

    # 각 meeting 튜플 x를 살펴보고, 종료시간(요소 x[1])을 기준으로 정렬     # 기본: 오름차순
    sorted_meetings = sorted(meetings, key=lambda x: x[1])  # 그리디 알고리즘 실행 준비
    
    selected = []       # selected: 배정된 회의 목록
    
    # 첫 번째 회의 선택

    selected.append(sorted_meetings[0])
    
    last_end_time = selected[0][1]  # end_time

    for i in sorted_meetings[1:]:
        if i[0] >= last_end_time:   # 문 열리는 시간을 확인 # 안전 장치(유효성 검사)
            selected.append(i)      # 회의 예약
            last_end_time = i[1]    # 회의 끝나는 시간을 업데이트 (다음 회의 대비)
    
    return len(selected), selected

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    meetings1 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9)]
    count1, selected1 = select_meetings(meetings1)
    print("=== 테스트 케이스 1 ===")
    print(f"전체 회의: {meetings1}")
    print(f"배정된 회의 개수: {count1}개")
    print(f"선택된 회의: {selected1}")
    print()
    
    # 테스트 케이스 2
    meetings2 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    count2, selected2 = select_meetings(meetings2)
    print("=== 테스트 케이스 2 ===")
    print(f"전체 회의: {len(meetings2)}개")
    print(f"배정된 회의 개수: {count2}개")
    print(f"선택된 회의: {selected2}")


