def print_book(book):
  print(book)
  
def count_words(book):
  words = book.split()
  words_count = len(words)

  return words_count

def count_letters(book):
  letters_dict = {}
  lower_book = book.lower()

  for letter in lower_book:
    if letter.isalpha() == False:
      continue
    if letter in letters_dict:
      letters_dict[letter] += 1
    else:
      letters_dict[letter] = 1
  
  return letters_dict

def sort_on_letter(letters_dict):
  return letters_dict["letter"]

def print_report(book_name, words_count, letters_dict):
  print(f'--- Begin report of books/{book_name}.txt ---')
  print(f'{words_count} words found in the document\n')
  
  letters_sorted = sorted(letters_dict)
  
  for letter in letters_sorted:
    count = letters_dict[letter]
    print(f"The '{letter}' character was found {count} times")
  
  print('--- End report ---')

def main():
  book_name = 'frankenstein'
  with open(f'./books/{book_name}.txt') as f:
    text = f.read()

    words_count = count_words(text)
    letters_dict = count_letters(text)
    print_report(book_name, words_count, letters_dict)
    
main()