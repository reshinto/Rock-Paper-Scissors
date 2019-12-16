// required for user input function
import java.util.Scanner;

// required for random function
import java.util.Random;

//import java.util.ArrayList;

import java.util.List;

public class RPSfunction {
    public static void main(String[] args) {
        intro();
    }
    
    public static String repeat(String str, int times) {
        return new String(new char[times]).replace("\0", str);
    }

    public static void intro() {
        String text = "Welcome to ROCK, PAPER, SCISSORS game!\n";
        int txt_size = text.length();
        System.out.println(repeat("#", txt_size));
        System.out.println(text);
        continue_game();
    }

    public static void continue_game() {
        String text = "Do you wish to play or continue playing (y/n)? ";
        Scanner choice = new Scanner(System.in);
        System.out.print(text);
        String choice_input = choice.nextLine().toLowerCase();
        if (choice_input.equals("y")) {
            play_game();
        } else if (choice_input.equals("n")) {
            System.out.println("\nThank you for playing!\n");
        } else {
            invalid_input();
            continue_game();
        }
    }

    public static void invalid_input() {
        String text = "You can only input y or n";
        int txt_size = text.length();
        System.out.println("\n"+repeat("!", txt_size));
        System.out.println(text);
        System.out.println(repeat("!", txt_size)+"\n");
    }

    public static void play_game() {
        String text = "\nEnter (r)ock, (p)aper, (s)cissors: ";
        int txt_size = text.length();
        System.out.println(repeat("=", txt_size));
        System.out.print(text);
        Scanner choice = new Scanner(System.in);
        String player = choice.nextLine().toLowerCase();
        
        Random rand = new Random();
        List<String> valid_moves = List.of("r","p","s");
        int randomIndex = rand.nextInt(valid_moves.size());
        String computer = valid_moves.get(randomIndex);
        rps_winner(player, computer);
    }

    public static void rps_winner(String player, String computer) {
        if (player.equals(computer)) {
            System.out.println("\nIt was a tie! you both moved: " + computer + "\n");
            continue_game();
        } else if (((player.equals("r")) && (computer.equals("s"))) || 
                   ((player.equals("p")) && (computer.equals("r"))) || 
                   ((player.equals("s")) && (computer.equals("p")))) {
            System.out.println("\nYou won! You moved: " + player + 
                               " | The computer moved: " + computer + "\n");
            continue_game();
        } else {
            // TODO else if player not in valid_moves
            System.out.println("\nYou lost! You moved: " + player + 
                               " | The computer moved: " + computer + "\n");
            continue_game();
        }
    }
}
