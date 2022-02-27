from collections import deque


def one_diff(word, change):
    wordlist = list(word)
    changelist = list(change)
    cnt = 0

    for w in wordlist:
        if w in changelist:
            changelist.remove(w)
    if len(changelist) == 1:
        return True
    else:
        return False

    """
    if cnt == len(word)-1:
        return True
    else:
        return False
    """


def solution(begin, target, words):
    answer = 0

    visited = [False] * len(words)

    if target not in words:
        return answer

    queue = deque([(begin, 0)])
    # visited[0] = True
    while queue:
        # print(queue)
        word = queue.popleft()

        if word[0] == target:
            return word[1]
        for i, w in enumerate(words):
            if one_diff(word[0], w) and not visited[i]:
                if w == target:
                    return word[1] + 1
                queue.append((w, word[1] + 1))
                visited[i] = True

    if visited[words.index(target)] == False:
        answer = 0

    return answer