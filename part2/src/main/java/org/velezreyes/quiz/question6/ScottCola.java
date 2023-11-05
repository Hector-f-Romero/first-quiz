package org.velezreyes.quiz.question6;

public class ScottCola implements Drink{
    private String name = "ScottCola";
    public static int price = 75;
    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean isFizzy() {
        return true;
    }
}
