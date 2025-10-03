def main():
    snake_case(input("camelCase: "))

def snake_case(prompt):
    result = ""
    for huruf in prompt:
        if huruf.isupper():
            result += "_" + huruf.lower()
        else:
            result += huruf
    print(result)

main()
