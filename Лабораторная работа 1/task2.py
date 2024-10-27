# TODO Найдите количество книг, которое можно разместить на дискете
floppy_volume = 1.44  # Объем дискеты в мегабайтах
book_pages = 100
lines_per_page = 50
sybmols_per_line = 25
symbol_volume = 4  # bytes

book_volume = symbol_volume*sybmols_per_line*lines_per_page*book_pages
calcs = (floppy_volume*1024**2)//book_volume

print("Количество книг, помещающихся на дискету:", int(calcs))
