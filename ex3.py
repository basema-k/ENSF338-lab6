# excercise 3

import sys

# node definition
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# build expression tree
def build_tree(tokens):
    stack = []

    for token in tokens:
        if token == ')':
            # build subtree when we see ')'
            right = stack.pop()
            operator = stack.pop()
            left = stack.pop()
            stack.pop()  # remove '('

            node = Node(operator)
            node.left = left
            node.right = right

            stack.append(node)

        elif token == '(':
            stack.append(token)

        elif token in ['+', '-', '*', '/']:
            stack.append(token)

        else:
            # number -> create node immediately
            stack.append(Node(int(token)))

    # final result is the root
    return stack[0]

# order evaluation
def evaluate(node):
    if node.left is None and node.right is None:
        return node.value

    left_val = evaluate(node.left)
    right_val = evaluate(node.right)

    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val

# main
if __name__ == "__main__":
    expression = input("Enter an arithmetic expression: ")
    tokens = expression.split()

    if len(tokens) == 1:
        print(int(tokens[0]))
    else:
        # only wrap if expression is not already fully parenthesized
        if tokens.count('(') == tokens.count(')') and tokens[0] != '(':
            tokens = ['('] + tokens + [')']
        root = build_tree(tokens)
        result = evaluate(root)
        print(result)