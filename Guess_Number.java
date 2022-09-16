package com.programs;

import java.util.Random;
import java.util.Scanner;

class Game{
   int rand_num;
   int user_input;
   int numberOfGuesses = 0;

   // Constructor to Generate a random number between   0 and 100;
   public Game(int n){
       Random rand = new Random();
       rand_num = rand.nextInt(n);
   }
   public void takeUserInput(){
       Scanner sc = new Scanner(System.in);
       System.out.println("Please Enter a number Between 0 to 100");
       user_input = sc.nextInt();
       numberOfGuesses++;// To know how many number of guesses...

   }
   public int isCorrectNumber(){
       if(rand_num == user_input){
           return 0;
       }else if(rand_num>user_input){
           return -1;
       }else{
           return 1;
       }
   }
}

public class Guess_Number {
    public static void main(String[] args) {
        Game myGame = new Game(101); // Random number generator
//        System.out.println("Random Number is: " +myGame.rand_num);
        while(true){
            myGame.takeUserInput();
            if(myGame.isCorrectNumber() == 0){
                System.out.println("Congratulations! You've guessed the number");
                System.out.println("Number of Guesses: "+myGame.numberOfGuesses);
                break;
            } else if(myGame.isCorrectNumber() == -1){
                System.out.println("Higher Number Please!");
            }else if(myGame.isCorrectNumber() == 1){
                System.out.println("Lower Number Please!");
            }
        }
    }
}
