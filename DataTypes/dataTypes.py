def main():
    fahr = int(input("Enter the temperature in F: "))
    cel = (fahr - 32) * 5.0/9.0
    print("the temperature in C is: ", cel)

if __name__ == "__main__":
    main()