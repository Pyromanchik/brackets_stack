from src.brackets_stack import Stack

def is_balanced(brackets: str) -> str:
    """Проверяет строку скобок на сбалансированность.

    Args:
        brackets (str): Строка, содержащая только скобки.

    Returns:
        str: "Сбалансированно" или "Несбалансированно".
    """
    stack = Stack()
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in brackets:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != bracket_map[char]:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


# Тесты
if __name__ == "__main__":
    # Сбалансированные
    assert is_balanced("(((([{}]))))") == "Сбалансированно"
    assert is_balanced("[([])((([[[]]])))]{}") == "Сбалансированно"
    assert is_balanced("{{[()]}}") == "Сбалансированно"

    # Несбалансированные
    assert is_balanced("}{") == "Несбалансированно"
    assert is_balanced("{{[(])]}}") == "Несбалансированно"
    assert is_balanced("[[{())}]") == "Несбалансированно"

    # Дополнительные тесты
    assert is_balanced("") == "Сбалансированно"
    assert is_balanced("()") == "Сбалансированно"
    assert is_balanced("(((") == "Несбалансированно"
    assert is_balanced(")))") == "Несбалансированно"

    print("✅ Все тесты пройдены!")