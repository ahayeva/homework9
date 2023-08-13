# def formatted_text(quote, author):
#     formatted_text = f'"{quote}"\n{author}'
#     print(formatted_text)
# formatted_text("Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.", "Bill Gates")
# #exercise 2
# def display_numbers(start, end):
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             print(num)
# display_numbers(10, 20)
# #exercise 3
# def display_square(side_length, symvol, filled):
#     if filled:
#         for _ in range(side_length):
#             print(symvol * side_length)
#     else:
#         print(symvol * side_length)
#         for _ in range(side_length - 2):
#             print(symvol + " " * (side_length - 2) + symvol)
#         print(symvol * side_length)
# display_square(5, "", True)
# display_square(5, "", False)
# #exercise 4
# def find_min(args):
#     return min(args)
# min_value = find_min(10, 5, 8, 20, 3)
# print(min_value)
# #exercise 5
# def calculate_product(start, end):
#     product = 1
#     for num in range(start, end + 1):
#         product *= num
#     return product
# product_result = calculate_product(1, 5)
# print(product_result)
# #exercise 6
# def count_digits(number):
#     return len(str(number))
# digit_count = count_digits(3456)
# print(digit_count)
# #exercise7
def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]
print(is_palindrome(123321))
print(is_palindrome(546645))
print(is_palindrome(421987))
if __name__ == "__main": 