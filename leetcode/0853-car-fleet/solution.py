from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)
    stack = []
    for pos, spd in cars:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)
    return len(stack)


# 範例測試
if __name__ == "__main__":
    print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # 輸出: 3
    print(carFleet(10, [3], [3]))                  # 輸出: 1
    print(carFleet(100, [0, 2, 4], [4, 2, 1]))         # 輸出: 1
