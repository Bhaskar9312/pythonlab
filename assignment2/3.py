def find_digits(N):
    count = 0
    for digit in str(N): 
        if digit != '0': 
            if N % int(digit) == 0:
                count += 1
    return count
def main():
    T = int(input("take number of test cases:"))
    for _ in range(T):
        N = int(input("give number for the current test case:"))
        print(find_digits(N))
main()