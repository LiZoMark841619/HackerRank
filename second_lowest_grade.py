if __name__ == '__main__':
    result = [[input(), float(input())] for _ in range(int(input()))]
    scores = [item[1] for item in result]
    scores = set(scores)
    scores = list(scores)
    scores.sort()

    names_after_scores = [item[0] for item in result]
    names_after_scores.sort()
    
    second_one = min(scores[1:])
    
    names_final = [item[0] for item in result if item[1] == second_one]
    names_final.sort()
    
    print(*names_final, sep='\n')
