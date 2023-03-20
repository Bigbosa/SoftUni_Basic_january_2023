book = input()
book_count = 0
current_book = input()
is_book_ = True
while current_book != "No More Books":
    if current_book == book:
        is_book_ = True
        print(f"You checked {book_count} books and found it.")
        break
    book_count += 1
    current_book = input()
else:
  print("The book you search is not here!")
  print(f"You checked {book_count} books.")