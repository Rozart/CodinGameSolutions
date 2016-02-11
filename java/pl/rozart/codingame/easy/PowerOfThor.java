package pl.rozart.codingame.easy;

import java.util.Scanner;

public class PowerOfThor {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt();
        int lightY = in.nextInt();
        int initialTX = in.nextInt();
        int initialTY = in.nextInt();

        int currentPosX = initialTX;
        int currentPosY = initialTY;
        while (true) {
            int remainingTurns = in.nextInt();

            String move = "";

            if (lightY > currentPosY) {
                move += "S";
                currentPosY++;
            } else if (lightY < currentPosY) {
                move += "N";
                currentPosY--;
            }

            if (lightX > currentPosX) {
                move += "E";
                currentPosX++;
            } else if (lightX < currentPosX) {
                move += "W";
                currentPosX--;
            }
            System.out.println(move);
        }
    }
}