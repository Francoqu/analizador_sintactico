import re

def check_parentheses(expression):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in matching.values():
            stack.append(char)
        elif char in matching.keys():
            if not stack or stack.pop() != matching[char]:
                return False
    return len(stack) == 0

def validate_expression(expression):
    tokens = re.split(r'(\s+|\+|-|\*|/|\(|\))', expression)
    tokens = [t for t in tokens if t.strip()]  
    last = None
    for token in tokens:
        if re.match(r'^[a-zA-Z0-9]+$', token): 
            if last == 'operand':
                return False  
            last = 'operand'
        elif token in '+-*/':
            if last != 'operand':
                return False  
            last = 'operator'
        elif token in '()':
            continue  
        else:
            return False  
    return last == 'operand'

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def build_expression_tree(tokens):
    stack = []
    operators = set("+-*/")
    for token in tokens:
        if token not in operators:
            stack.append(Nodo(token))
        else:
            node = Nodo(token)
            node.derecha = stack.pop()
            node.izquierda = stack.pop()
            stack.append(node)
    return stack.pop()

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.izquierda)
        print(root.valor, end=" ")
        inorder_traversal(root.derecha)

def analyze_expression(expression):
    print(f"Analizando expresión: {expression}")
    if not check_parentheses(expression):
        return "Error: Paréntesis desbalanceados"
    if not validate_expression(expression):
        return "Error: Expresión inválida "
    
    tokens = re.split(r'(\s+|\+|-|\*|/|\(|\))', expression)
    tokens = [t for t in tokens if t.strip()]
    tree = build_expression_tree(tokens)
    print("Recorrido inorden :")
    inorder_traversal(tree)
    print()
    return " Valida"

if __name__ == "__main__":
    expr = "5 * (3 + 2)"
    result = analyze_expression(expr)
    print(result)
