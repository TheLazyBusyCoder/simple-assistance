from word2number import w2n

class Math:
    def __init__(self):
        pass
    
    def calculate_expression(self , expression , oneone):
        try:
            if 'into' in expression:
                expression = expression.replace('into' , '*')
            if 'x' in expression:
                expression = expression.replace('x' , '*')
            print(f"Expression: {expression}")
            result = eval(expression)
            oneone.speak("Anser is " + str(result))
        except Exception as e:
            oneone.speak("Expression error")
