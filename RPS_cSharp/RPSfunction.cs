using System;
using System.Collections.Generic;

public class RPSfunction {
  public static void Main() {
    intro();
  }

  public static void intro() {
    string text = "Welcome to ROCK, PAPER, SCISSORS game!\n";
    int txtSize = text.Length;
    Console.WriteLine(repeat('#', txtSize));
    Console.WriteLine(text);
    continueGame();
  }

  public static String repeat(char str, int times) {
    return new String(str, times);
  }

  public static void continueGame() {
      string text = "Do you wish to play or continue playing (y/n)? ";
      Console.Write(text);
      char choice = Console.ReadKey().KeyChar;
      char choiceInput = choice;
      if (choiceInput.Equals('y')) {
          playGame();
      } else if (choiceInput.Equals('n')) {
          Console.WriteLine("\nThank you for playing!\n");
      } else {
          invalidInput();
          continueGame();
      }
  }

  public static void invalidInput() {
      string text = "You can only input y or n";
      int txtSize = text.Length;
      Console.WriteLine("\n" + repeat('!', txtSize));
      Console.WriteLine(text);
      Console.WriteLine(repeat('!', txtSize) + "\n");
  }

  public static void playGame() {
      string text = "\nEnter (r)ock, (p)aper, (s)cissors: ";
      int txtSize = text.Length;
      Console.WriteLine("\n" + repeat('=', txtSize));
      Console.Write(text);
      char choice = Console.ReadKey().KeyChar;
      /* var player = choice.ToLower(); */
      Console.WriteLine($"player choice: {choice}");
      char player = choice;

      Random rand = new Random();
      List<char> validMoves = new List<char>() {'r','p','s'};
      int randomIndex = rand.Next(validMoves.Count);
      char computer = validMoves[randomIndex];
      rpsWinner(player, computer);
  }

  public static void rpsWinner(char player, char computer) {
      if (player.Equals(computer)) {
          Console.WriteLine("\nIt was a tie! you both moved: " + computer + "\n");
          continueGame();
      } else if (((player.Equals('r')) && (computer.Equals('s'))) ||
                 ((player.Equals('p')) && (computer.Equals('r'))) ||
                 ((player.Equals('s')) && (computer.Equals('p')))) {
          Console.WriteLine("\nYou won! You moved: " + player +
                             " | The computer moved: " + computer + "\n");
          continueGame();
      } else {
          // TODO else if player not in valid_moves
          Console.WriteLine("\nYou lost! You moved: " + player +
                             " | The computer moved: " + computer + "\n");
          continueGame();
      }
  }
}
