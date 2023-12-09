from f1_display_books import display_books
from aux6_sort_books import ask_sort_books

display_books()
ask_sort_books()

# Notes:
# If there are duplicate copies but different date purchased/status, it works but doesn't order them in any particular way.
# If sorted by date of purchase, only sorts by the first digit in date. Probably better to not include the option?
