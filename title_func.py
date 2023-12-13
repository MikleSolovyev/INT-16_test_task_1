# O(n) - time complexity
# O(1) - space complexity
def title(input_str: str) -> str:
    result = list(input_str)
    is_prev_alpha = False
    for i in range(len(result)):
        if result[i].isalpha():
            if not is_prev_alpha:
                result[i] = result[i].upper()

            is_prev_alpha = True
        else:
            is_prev_alpha = False

    return ''.join(result)


if __name__ == '__main__':
    print(title('тесТОвое задание для pt'))
