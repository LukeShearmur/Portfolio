package com.Shrubby;

import java.lang.String;
import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Random random = new Random();
        int lives = 5;

        String[] words = {"time", "fruit", "static", "dota", "cake","camera"};

        System.out.println("Welcome to Hangman");
        System.out.println("Guess a letter by typing it in, every wrong guess costs you a life");
        System.out.println("You have 5 lives, good luck");

        String wordToGuess = words[random.nextInt(words.length)];
        List<String> playerGuesses = new ArrayList<String>();

        for(int i=0; i < wordToGuess.length(); i++) {
            playerGuesses.add("_");
        }

        while(lives >0){

            if(playerGuesses.indexOf("_")== -1){

                System.out.println("Well Done, the word was " + wordToGuess);
                break;

            }
            System.out.println(String.join(" ",playerGuesses));

            String input = sc.nextLine();

           if(wordToGuess.indexOf(input)== -1){
              lives--;
               System.out.println(lives+" lives left");
           }else {

               for (int i=0;i <wordToGuess.length(); i++){

                   char c = wordToGuess.charAt(i);

                   if (c == input.charAt(0)){

                       playerGuesses.set(i,input);
                   }
               }
           }
        }
        if(lives==0) {
            System.out.println("You are dead");
        }
    }
}
