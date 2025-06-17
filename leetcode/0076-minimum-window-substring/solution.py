# 最小覆蓋子字串演算法
from collections import Counter  # 匯入 Counter 用於計算字元出現次數


def min_window(s: str, t: str) -> str:
    need = Counter(t)  # 建立需求字典，記錄 t 中每個字元需要的數量
    window = {}  # 用來記錄目前視窗內的字元數量
    left = 0  # 左指標，視窗左邊界
    right = 0  # 右指標，視窗右邊界
    valid = 0  # 已滿足需求的字元種類數
    start = 0  # 最小視窗的起始位置
    length = float('inf')  # 最小視窗長度，初始為無限大

    while right < len(s):  # 右指標未到字串尾
        c = s[right]  # 取得右指標字元
        right += 1  # 右指標右移
        if c in need:  # 若該字元在需求中
            window[c] = window.get(c, 0) + 1  # 更新視窗內字元數
            if window[c] == need[c]:  # 若該字元數量滿足需求
                valid += 1  # 有一種字元滿足
        # 當所有需求字元都滿足
        while valid == len(need):
            if right - left < length:  # 若當前視窗更小
                start = left  # 更新最小視窗起點
                length = right - left  # 更新最小長度
            d = s[left]  # 取得左指標字元
            left += 1  # 左指標右移
            if d in need:  # 若該字元在需求中
                if window[d] == need[d]:  # 若移除後不再滿足需求
                    valid -= 1  # 有一種字元不滿足
                window[d] -= 1  # 更新視窗內字元數
    return "" if length == float('inf') else s[start:start+length]  # 回傳結果


if __name__ == "__main__":
    # 範例測試
    print(min_window("ADOBECODEBANC", "ABC"))  # 輸出：BANC
    print(min_window("a", "a"))                # 輸出：a
    print(min_window("a", "aa"))               # 輸出：
