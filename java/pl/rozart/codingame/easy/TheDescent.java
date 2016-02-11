package pl.rozart.codingame.easy;

import java.util.Arrays;
import java.util.Scanner;

public class TheDescent {

    private static final int MAX_SPACE_X = 7;

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);

        while (true) {
            int spaceX = in.nextInt();
            int spaceY = in.nextInt();

            int[] mountains = new int[8];
            for (int i = 0; i < 8; i++) {
                mountains[i] = in.nextInt();
            }

            int[] mountainsClone = mountains.clone();
            Arrays.sort(mountainsClone);
            int highestMountainHeight = mountainsClone[mountainsClone.length - 1];
            boolean isHighestMountain = mountains[spaceX] == highestMountainHeight;

            if (isHighestMountain) {
                System.out.println("FIRE");
            } else {
                System.out.println("HOLD");
            }
        }
    }
}

