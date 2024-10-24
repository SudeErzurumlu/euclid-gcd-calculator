# main.py

import argparse
from euclid_gcd.gcd import euclid_gcd
from euclid_gcd.utils import validate_input

def main():
    parser = argparse.ArgumentParser(description="Calculate the Greatest Common Divisor (GCD) of two numbers using Euclid's algorithm.")
    parser.add_argument("a", type=int, help="First non-negative integer.")
    parser.add_argument("b", type=int, help="Second non-negative integer.")
    args = parser.parse_args()

    try:
        # Validate inputs
        a, b = validate_input(args.a, args.b)

        # Calculate GCD
        result = euclid_gcd(a, b)

        # Output the result
        print(f"The GCD of {a} and {b} is: {result}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
