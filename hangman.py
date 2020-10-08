# -------- Hangman ---------------

from random import randint
def hang():
  words = ["apple", "orange", "pear", "book",'rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']
  word_count = len(words)
  word_index = randint(0, word_count-1)
  selected_word = words[word_index]
  hidden_word = ["_"]*len(selected_word)

  while True:

    print(' '.join(hidden_word))
  
    print("Guess a letter...")
    guess = input().lower()

    while len(guess) > 1:
      print("Enter only one letter!")
      guess = input().lower()
  
    if guess in selected_word:
      print("Nope, Guess A Differnt Letter")
      for index, letter in enumerate(selected_word):
        if guess == letter:
          hidden_word[index] = guess

    else:
      print("Not present")


    print() 

    if '_' not in hidden_word:
        print("       __        _")
        print("     _/  \    _(\(o" )
        print("    /     \  /  _  ^^^o")
        print("   /   !   \/  ! '!!!v'"  )
        print("   !  !  \ _' ( \____")
        print("   ! . \ _!\   \===^\)")
        print("    \ \_!  / __!"  )
        print("     \!   /    \ ")
        print("(\_      _/   _\ )")
        print(" \ ^^--^^ __-^ /(__")
        print("  ^^----^^    '^--v'")
        print("\u001b[32m \u001b[41mGOOD JOB\u001b[0m")
        print(u"\u001B[0m")
