package com.programs;
import java.util.Random;
import java.util.Scanner;

public class RPS_Game {
    public static void main(String[] args) {
            // 0 for rock
            // 1 for paper
            // 2 for scissors
            Scanner sc = new Scanner(System.in);
            System.out.println("Input 0 for Rock, 1 for Paper, 2 for Scissors");
            int user_choice = sc.nextInt();
            Random random = new Random();
            int computer_choice = random.nextInt(3);

            if (user_choice == computer_choice) {
                System.out.println("Draw!");
            } else if (user_choice == 0 && computer_choice == 2 || user_choice == 2 && computer_choice == 1 || user_choice == 1
                    && computer_choice == 0) {
                System.out.println("Woohooo! You win");
            } else {
                System.out.println("Computer Win");
            }
            if(computer_choice == 0) {
                System.out.println("Computer Choice: Rock");
            }else if(computer_choice == 1) {
                System.out.println("Computer Choice: Paper");
            }else{
                System.out.println("Computer Choice: Scissors");
        }
    }
}
