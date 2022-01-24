def solution(skill, skill_trees):
    skill = list(skill)
    cnt  = len(skill_trees)
    for i in skill_trees:
        start = 0
        not_exist = list(reversed(skill))
        del not_exist[-1]
        for j in i:
            if j == skill[start]:
                start += 1
                if len(not_exist) > 0:
                    del not_exist[-1]
            elif j in not_exist:
                cnt -= 1
                break
            if start >= len(skill):
                start -= 1
    return cnt