import re


def palindrome(s: str) -> bool:
    s = s.lower()
    s = s.replace(" ", "")
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    for s_index in range(int(len(s) / 2)):
        if s[s_index] != (s[(s_index + 1) * (-1)]):
            return False

    return True


if __name__ == "__main__":
    print(palindrome("Was it, a car or a cat I saw?"))
