list_of_words="What is the difference between coronavirus and COVID-19".split(' ')
print(list_of_words)


def lengths(list_of_words):
  total_length=0
  for word in list_of_words:
    total_length = len(list(word)) + total_length
  return total_length


number_of_letters = lengths(list_of_words)
number_of_words = len(list_of_words)
print(number_of_letters / number_of_words)
