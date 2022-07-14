package com.Shrubby;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int health = 1;

//        Enemy enemy = new Enemy();
//
//        enemy.buildEnemy(1);


        while (health !=0) {
            Character player = new Character();



            System.out.println("Choose from two characters");
            System.out.println("1 = Jet");
            System.out.println("2 = Jinx");

            int input = sc.nextInt();


            if (input == 1) {
                player.buildJet();
                player.Health = player.maxHealth;
                health = player.Health;

                System.out.println("HP = " + health);

                health = 0;


            } else if (input == 2) {
                player.buildJinx();
                health = player.Health;

                System.out.println("HP = " + health);

                health = 0;


            } else {
                System.out.println("Incorrect input");
                System.out.println(" ");
            }


        }
    }
}
