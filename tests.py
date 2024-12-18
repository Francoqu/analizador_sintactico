from main import analyze_expression

test_cases = [
    "((a + b) * c)",   
    "5 * (3 + 2)",    
    "(a + b)) * c",    
    "5 * + (3 2)",     
    "(x / y) + z",     
]

for i, expr in enumerate(test_cases, 1):
    print(f"Prueba {i}: {expr}")
    print(analyze_expression(expr))
    print("-" * 40)
