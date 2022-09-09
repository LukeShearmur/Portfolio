package com.Shrubby;

import java.util.Random;

public class Die {

    int numSides;

    Random r;

    Die(int numSides){

        this.numSides = numSides;

        this.r = new Random();

    }

    public int roll(){

        int randomOne = r.nextInt(this.numSides)+1;
        return randomOne;
    }
}

