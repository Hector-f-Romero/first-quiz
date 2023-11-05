package org.velezreyes.quiz.question6;

import java.util.Arrays;
import java.util.Objects;

public class VendingMachineImpl implements VendingMachine{

  // Create a static variable for use singleton pattern and only has one instance of VendingMachine interface.
  private static VendingMachine instance;
  private int currentMoney = 0;
  // Define the available drinks in this vending machine.
  private final String[] availableDrinks = {"ScottCola","KarenTea"};

  public static VendingMachine getInstance() {
    if (instance == null) {
      // If the instance has not been created, we create it.
      instance = new VendingMachineImpl();
    }
    return instance;
  }

  @Override
  public void insertQuarter() {
    currentMoney += 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {

    // Verify if the vending machine has the drink requested in its inventory.
    if(!Arrays.asList(availableDrinks).contains(name)){
      throw new UnknownDrinkException();
    }

    if(currentMoney < ScottCola.price && Objects.equals(name,"ScottCola")){
      throw new NotEnoughMoneyException();
    }

    if(currentMoney < KarenTea.price && Objects.equals(name,"KarenTea")){
      throw new NotEnoughMoneyException();
    }

    if(currentMoney>=75 && Objects.equals(name, "ScottCola")){
      currentMoney -= 75;
      return new ScottCola();
    }

    if(currentMoney>=100 && Objects.equals(name, "KarenTea")){
      currentMoney -= 100;
      return new KarenTea();
    }

    return null;
  }
}
