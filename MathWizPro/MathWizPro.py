import math
import numpy as np

def solve_arithmetic(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "Invalid expression"

def solve_equation(equation):
    try:
        variable, expression = equation.split('=')
        variable = variable.strip()
        expression = expression.strip()
        solution = solve_arithmetic(expression)
        return f"{variable} = {solution}"
    except:
        return "Invalid equation format"

def solve_quadratic(a, b, c):
    try:
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return "No real roots"
        elif discriminant == 0:
            root = -b / (2*a)
            return f"Single root: {root}"
        else:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            return f"Root 1: {root1}, Root 2: {root2}"
    except:
        return "Invalid coefficients"

def solve_linear_system(coeff_matrix, const_vector):
    try:
        solutions = np.linalg.solve(coeff_matrix, const_vector)
        return solutions
    except:
        return "No unique solution or invalid input"

def calculate_area(shape, *args):
    try:
        if shape == 'rectangle' and len(args) == 2:
            width, height = args
            area = width * height
            return f"Area: {area}"
        elif shape == 'circle' and len(args) == 1:
            radius = args[0]
            area = math.pi * radius**2
            return f"Area: {area}"
        else:
            return "Invalid shape or parameters"
    except:
        return "Invalid parameters"

def calculate_volume(shape, *args):
    try:
        if shape == 'sphere' and len(args) == 1:
            radius = args[0]
            volume = 4/3 * math.pi * radius**3
            return f"Volume: {volume}"
        else:
            return "Invalid shape or parameters"
    except:
        return "Invalid parameters"

def calculate_compound_interest(principal, rate, time):
    try:
        amount = principal * (1 + rate/100)**time
        interest = amount - principal
        return f"Compound Interest: {interest:.2f}"
    except:
        return "Invalid input"

def generate_fibonacci_sequence(n):
    try:
        fibonacci = [0, 1]
        while len(fibonacci) < n:
            next_num = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(next_num)
        return fibonacci
    except:
        return "Invalid input"

def calculate_trigonometry(operation, angle_degrees):
    try:
        angle_radians = math.radians(angle_degrees)
        if operation == 'sine':
            result = math.sin(angle_radians)
        elif operation == 'cosine':
            result = math.cos(angle_radians)
        elif operation == 'tangent':
            result = math.tan(angle_radians)
        else:
            return "Invalid trigonometric operation"
        return f"{operation}({angle_degrees}°) = {result:.4f}"
    except:
        return "Invalid input"

def convert_units(value, from_unit, to_unit):
    conversions = {
        'meters': {'feet': 3.281, 'inches': 39.37},
        'feet': {'meters': 0.3048, 'inches': 12},
        'inches': {'meters': 0.0254, 'feet': 0.0833}
    }
    
    try:
        converted_value = value * conversions[from_unit][to_unit]
        return f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit}"
    except KeyError:
        return "Invalid units"
    except:
        return "Invalid input"

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_range(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

while True:
    print("MathWiz Pro")
    print("1. Solve arithmetic expression")
    print("2. Solve equation")
    print("3. Solve quadratic equation")
    print("4. Solve system of linear equations")
    print("5. Calculate area")
    print("6. Calculate volume")
    print("7. Calculate compound interest")
    print("8. Generate Fibonacci sequence")
    print("9. Perform trigonometric calculation")
    print("10. Convert units")
    print("11. Find prime numbers in a range")
    print("12. Find greatest common divisor (GCD)")
    print("13. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        expression = input("Enter arithmetic expression: ")
        result = solve_arithmetic(expression)
        print("Result:", result)
        
    elif choice == '2':
        equation = input("Enter equation (e.g., 'x + 2 = 10'): ")
        solution = solve_equation(equation)
        print("Solution:", solution)
        
    elif choice == '3':
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        roots = solve_quadratic(a, b, c)
        print("Quadratic equation roots:", roots)
        
    elif choice == '4':
        try:
            num_equations = int(input("Enter the number of equations: "))
            coeff_matrix = []
            const_vector = []
            for i in range(num_equations):
                coefficients = [float(coeff) for coeff in input(f"Enter coefficients for equation {i+1}: ").split()]
                const = float(input(f"Enter constant for equation {i+1}: "))
                coeff_matrix.append(coefficients)
                const_vector.append(const)
            solutions = solve_linear_system(coeff_matrix, const_vector)
            print("Solution(s):", solutions)
        except ValueError:
            print("Invalid input")
        
    elif choice == '5':
        shape = input("Enter shape ('rectangle' or 'circle'): ")
        args = [float(arg) for arg in input("Enter parameters: ").split()]
        area_result = calculate_area(shape, *args)
        print(area_result)
        
    elif choice == '6':
        shape = input("Enter shape ('sphere'): ")
        args = [float(arg) for arg in input("Enter parameters: ").split()]
        volume_result = calculate_volume(shape, *args)
        print(volume_result)
        
    elif choice == '7':
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter interest rate (%): "))
        time = float(input("Enter time (years): "))
        interest_result = calculate_compound_interest(principal, rate, time)
        print(interest_result)
        
    elif choice == '8':
        n = int(input("Enter the number of Fibonacci sequence terms: "))
        fibonacci_sequence = generate_fibonacci_sequence(n)
        print("Fibonacci sequence:", fibonacci_sequence)
        
    elif choice == '9':
        operation = input("Enter trigonometric operation ('sine', 'cosine', 'tangent'): ")
        angle_degrees = float(input("Enter angle in degrees: "))
        trig_result = calculate_trigonometry(operation, angle_degrees)
        print(trig_result)
        
    elif choice == '10':
        value = float(input("Enter value: "))
        from_unit = input("Enter source unit: ")
        to_unit = input("Enter target unit: ")
        conversion_result = convert_units(value, from_unit, to_unit)
        print(conversion_result)
        
    elif choice == '11':
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        primes = find_primes_in_range(start, end)
        print("Prime numbers:", primes)
        
    elif choice == '12':
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        gcd_result = find_gcd(a, b)
        print("GCD:", gcd_result)
        
    elif choice == '13':
        print("Exiting...")
        break
        
    else:
        print("Invalid choice. Please select a valid option.")
