package com.Shrubby;

import java.util.Random;

public class NumberGame {

    int lives = 5;
    int num;

    NumberGame() {

        Random generator = new Random();
        this.num = generator.nextInt(10) + 1;

    }

    public String guess(int guessNum) {

        this.lives--;

        if (this.num == guessNum) {
            this.lives = 0;
            return "Correct, Well Done!";
        }
        else if (this.lives == 0) {
            return "Game Over!";
        }
        else if (this.num < guessNum) {
            return "Lower, you have " + lives + " more tries";
        }
        else {
            return "Higher, you have " + lives + " more tries";
        }
    }
}

