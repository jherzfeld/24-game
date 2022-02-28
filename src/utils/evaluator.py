

class Lexer():
    """
    Create a List of tokens based on string input
    """

    def __init__(self):
        self.expression = None
        self.current_character = None

    def next_character(self):
        try:
            self.current_character = next(self.expression)
        except StopIteration:
            self.current_character = None

    def create_token_list(self, expression):
        self.expression = iter(expression)
        self.next_character()
        token_list = []
        
        if self.current_character == None:
            raise Exception("Invalid Expression!")

        while self.current_character != None:

            if self.current_character == ' ':
                self.next_character()
            elif self.current_character.isdigit():
                token_list.append(self.get_number())
            elif self.current_character == '+':
                self.next_character()
                token_list.append({'PLUS': ''})
            elif self.current_character == '-':
                self.next_character()
                token_list.append({'MINUS': ''})
            elif self.current_character == '/':
                self.next_character()
                token_list.append({'DIVIDE': ''})
            elif self.current_character == '*':
                self.next_character()
                token_list.append({'MULTIPLY': ''})
            elif self.current_character == '(':
                self.next_character()
                token_list.append({'LPARA': ''})
            elif self.current_character == ')':
                self.next_character()
                token_list.append({'RPARA': ''})
            else:
                raise Exception("Invalid Character")
                        
        return token_list

    def get_number(self):
        number_str = self.current_character
        self.next_character()

        while self.current_character != None and self.current_character.isdigit():
            number_str += self.current_character
            self.next_character()

        return {'NUMBER': int(number_str)}


class Parser():
    """
    Create parse tree based on list of tokens
    """

    def __init__(self):
        self.tokens = None
        self.current_token = None

    def next_token(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
 
    def get_token_type(self):
        if self.current_token != None:
            token_type = list(self.current_token.keys())[0]
        else:
            token_type = None
        return token_type

    def get_token_value(self):
        if self.current_token != None:
            token_value = list(self.current_token.values())[0]
        else:
            token_value = None
        return token_value

    def parse(self, tokens):
        self.tokens = iter(tokens)
        self.next_token()

        if self.current_token == None:
            raise Exception("Invalid Expression")

        result = self.create_parse_tree()

        if self.current_token != None:
            raise Exception("Invalid Expression")

        return result

    def create_parse_tree(self):
        parse_tree = self.term()
        token_type = self.get_token_type()

        while self.current_token != None and token_type in ('PLUS', 'MINUS'):
            if token_type == 'PLUS':
                self.next_token()
                parse_tree = {'ADD': [parse_tree, self.term()]}

            elif token_type == 'MINUS':
                self.next_token()
                parse_tree = {'SUBTRACT': [parse_tree, self.term()]}

            token_type = self.get_token_type()
        
        return parse_tree

    def term(self):
        parse_tree = self.factor()
        token_type = self.get_token_type()

        while self.current_token != None and token_type in ('MULTIPLY', 'DIVIDE'):
            if token_type == 'MULTIPLY':
                self.next_token()
                parse_tree = {'MULTIPLY': [parse_tree, self.factor()]}
            elif token_type == 'DIVIDE':
                self.next_token()
                parse_tree = {'DIVIDE': [parse_tree, self.factor()]}

            token_type = self.get_token_type()

        return parse_tree

    def factor(self):
        token_type = self.get_token_type()
        token_value = self.get_token_value()
        
        if token_type == 'LPARA':
            self.next_token()
            parse_tree = self.create_parse_tree()
            
            token_type = self.get_token_type()
            if token_type != 'RPARA':
                raise Exception("Invalid Expression")
            
            self.next_token()
            return parse_tree
        elif token_type == 'NUMBER':
            self.next_token()
            return {'NUMBER': token_value}
        elif token_type == 'PLUS':
            self.next_token()
            return {'MULTIPLY': [{'NUMBER': 1}, self.factor()]}
        elif token_type == 'MINUS':
            self.next_token()
            return {'MULTIPLY': [{'NUMBER': -1}, self.factor()]}
        else:
            raise Exception("Invalid Expression")


class Interpreter():
    """
    Evaluate a mathematical expression input as a string.
    The expression can contain integer numbers and the operators:

    +:  Addition
    -:  Substraction
    *:  Multiplication
    /:  Division
    (): Paranthesis
    """

    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()

    def get_current_operation(self):
        try:
            self.current_operation = list(self.current_expression.keys())[0]
            self.current_value = list(self.current_expression.values())[0]
        except:
            self.current_operation = None
            self.current_value = None

    def interpret_expression(self, parse_tree):
        self.current_expression = parse_tree
        self.get_current_operation()

        if self.current_operation == 'NUMBER':
            result = self.current_value
        elif self.current_operation == 'ADD':
            term_A, term_B =  self.current_value
            term_A_value = self.interpret_expression(term_A)
            term_B_value = self.interpret_expression(term_B)

            result = term_A_value + term_B_value
        elif self.current_operation == 'SUBTRACT':
            term_A, term_B =  self.current_value
            term_A_value = self.interpret_expression(term_A)
            term_B_value = self.interpret_expression(term_B)

            result = term_A_value - term_B_value
        elif self.current_operation == 'MULTIPLY':
            term_A, term_B =  self.current_value
            term_A_value = self.interpret_expression(term_A)
            term_B_value = self.interpret_expression(term_B)

            result = term_A_value * term_B_value
        elif self.current_operation == 'DIVIDE':
            term_A, term_B =  self.current_value
            term_A_value = self.interpret_expression(term_A)
            term_B_value = self.interpret_expression(term_B)

            result = term_A_value / term_B_value
        else:
            raise Exception("Invalid Expression!")

        return result

    def evaluate(self, expression):
        token_list = self.lexer.create_token_list(expression)
        parse_tree = self.parser.parse(token_list)
        result     = self.interpret_expression(parse_tree) 

        return result
