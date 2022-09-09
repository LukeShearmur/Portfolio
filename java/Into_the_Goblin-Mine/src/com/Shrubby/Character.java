package com.Shrubby;

public class Character {

    public String Name;
    public int maxHealth;
    public int Health = maxHealth;
    public int maxMana;
    public int Mana;
    public int Intelligence;
    public int Dexterity;
    public int Strength;
    public double Attack;

    public void buildJet() {

        Name = "Jet";
        maxHealth = 40;
        maxMana = 0;
        Intelligence = 5;
        Dexterity = 15;
        Strength = 10;
        Attack = Dexterity * 1.5;

        Health = maxHealth;
        Mana = maxMana;

        System.out.println("Name = " + Name);
        System.out.println("MaxHP = " + maxHealth);
        System.out.println("MaxMana = " + maxMana);
        System.out.println("Intelligence = " + Intelligence);
        System.out.println("Dexterity = " + Dexterity);
        System.out.println("Strength = " + Strength);



    }

    public void buildJinx() {

        Name = "Jinx";
        maxHealth = 30;
        maxMana = 50;
        Intelligence = 20;
        Dexterity = 5;
        Strength = 5;
        Attack = Intelligence*1.5;

        Health = maxHealth;
        Mana = maxMana;

        System.out.println("Name = " + Name);
        System.out.println("MaxHP = " + maxHealth);
        System.out.println("MaxMana = " + maxMana);
        System.out.println("Intelligence = " + Intelligence);
        System.out.println("Dexterity = " + Dexterity);
        System.out.println("Strength = " + Strength);

    }


}
