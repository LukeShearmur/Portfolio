package com.Shrubby;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        boolean running = true;

        Scanner sc = new Scanner(System.in);

        while (running) {

            System.out.println("Press Enter to Roll a 6 sided Die, define number of side with 'd' and the number of sides. Type exit to quit");

            String command = sc.nextLine();

            if(command.equals("Exit")){
                running = false;
            }
            else if (command.startsWith("d")){

                String withoutD = command.replace("d","");

                int numSides = Integer.parseInt(withoutD);

                Die die = new Die(numSides);

                System.out.println(die.roll());
            }
            else {

                Die die = new Die(6);

                System.out.println(die.roll());



            }



        }




    }
}
