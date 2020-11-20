# Calculate factorial using generators
# Time complexity for below program is 0(2N) -> O(N)

def calculate_factors(input_number):
    for num in range(1, input_number+1):
        if input_number % num == 0:
            yield num
print([factors for factors in calculate_factors(24)])
