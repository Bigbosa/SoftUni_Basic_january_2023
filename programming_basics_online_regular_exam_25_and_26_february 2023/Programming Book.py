price_for_one_page = float(input())
price_print = float(input())
percent_off = int(input())
sum_for_design = float(input())
sum_ = int(input())

BOOK_PAGE = 899
COVER = 2

price = price_for_one_page * BOOK_PAGE + price_print * COVER
percent = (price * percent_off) / 100

percent_2 = price - percent

design = percent_2 + sum_for_design

total = ( design * sum_) / 100
total_price = design - total

print(f"Avtonom should pay {total_price:.2f} BGN.")