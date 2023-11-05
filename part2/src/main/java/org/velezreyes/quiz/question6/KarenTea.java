package org.velezreyes.quiz.question6;

public class KarenTea implements Drink{

    private String name = "KarenTea";
    public static int price = 100;

    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean isFizzy() {
        return false;
    }
}
