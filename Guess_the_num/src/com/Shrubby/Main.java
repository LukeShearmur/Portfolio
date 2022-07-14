package com.Shrubby;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        NumberGame game = new NumberGame();

        Scanner sc = new Scanner(System.in);

        while (game.lives != 0) {

            System.out.println("Guess a number between 1 - 10. Good luck! :D ");

            int input = sc.nextInt();

            System.out.println(game.guess(input));
        }
    }
}
