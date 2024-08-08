def main():
   from Live import welcome_user
   welcome_user()
   from Live import load_game, load_difficulty
   from Score import clear_winning_points, add_score
   clear_winning_points()
   from Score import current_score


   clear_winning_points()
   print(f"The current score is {current_score}")
   global remaining_attemts
   global game
   remaining_attemts = 3
   def remaining_attempts_count():
      global game
      global remaining_attemts
#      remaining_attemts =0
      while remaining_attemts > 0:
         print(f"""
   Your remaining atempts are {remaining_attemts}!""")
         load_game()
         load_difficulty()
         from Live import name, game, difficulty
         from Score import write_to_scores_file
         global game
         if game == 1:
            import MemoryGame
            MemoryGame.play_memory_game()
            remaining_attemts -= 1
            write_to_scores_file()
         elif game == 2:
            import GuessGame
            GuessGame.guess_game()
            remaining_attemts -= 1
            write_to_scores_file()
         elif game == 3:
            import CurrencyRouletteGame
            CurrencyRouletteGame.play()
            remaining_attemts -= 1
            write_to_scores_file()
         return remaining_attempts_count()
      print("""
You are out of attempts!
""")
#      from ScoreTable import sorting
#      sorting()
      print("""
----------------------------------------------------------
The end!!!
----------------------------------------------------------
""")
      from Score import current_score
      global current_score
      print(f"Your total score from the games is: {current_score}")
      # here show the best ones
      return main()
   remaining_attempts_count()
main()