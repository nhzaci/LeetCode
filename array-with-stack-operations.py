class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        actions = []
        push_pop = ["Push", "Pop"]
        current_index = 0
        for i in range(1, max(target) + 1):
            if i == target[current_index]:
                actions.append("Push")
                current_index += 1
                if current_index > len(target) - 1:
                    break
            else:
                actions.extend(push_pop)
        return actions
