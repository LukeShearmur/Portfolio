package com.Shrubby;

public class Enemy {

    public int enemyMaxhp;
    public int enemyHp;
    public int enemydmg;


    public void buildEnemy(int enemyType){

        switch(enemyType){
            case 1 :
                enemyMaxhp = 40;
                enemyHp = enemyMaxhp;
                enemydmg = 7;

                break;
            case 2 :
                enemyMaxhp = 70;
                enemyHp = enemyMaxhp;
                enemydmg = 10;
                break;
            case 3 :
                enemyMaxhp = 100;
                enemyHp = enemyMaxhp;
                enemydmg = 15;
                break;
        }

        System.out.println("HP = " + enemyHp);
        System.out.println("Dmg = " + enemydmg);

    }

}
