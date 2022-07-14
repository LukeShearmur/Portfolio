package com.Shrubby;

import java.util.Scanner;

public class Story {

        public static void intro(){
            System.out.println("Jet walks into the Goblin mine in search of ore and treasure");
            System.out.println("Into the dark mine he treads, slowly moving forward");
            System.out.println("In front of him are three passages");
            System.out.println("What does he do?");

            Scanner sc = new Scanner(System.in);

            String input = sc.nextLine();

            if (input == "left") {

                System.out.println("Jet turns to his left, following the passage down deeper into the mine");
                System.out.println("Nearly tripping over rocks he stumbles into a door");
                System.out.println("Does he try to open it?");

            } else {
                System.out.println("Jet stays still");
            }
        }
    }
