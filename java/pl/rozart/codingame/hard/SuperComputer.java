package pl.rozart.codingame.hard;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class SuperComputer {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        List<Operation> operations = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int J = in.nextInt();
            int D = in.nextInt();
            operations.add(new Operation(J, D));
        }

        Collections.sort(operations);

        List<Operation> resultOperations = new ArrayList<>();
        Operation currentOperation = operations.get(0);
        resultOperations.add(currentOperation);
        for (int i = 1; i < operations.size(); i++) {
            if (operations.get(i).getStartDay() != currentOperation.getStartDay()) {
                if (operations.get(i).getStartDay() >= currentOperation.getEndDay()) {
                    resultOperations.add(operations.get(i));
                    currentOperation = operations.get(i);
                }
            }
        }

        System.err.print(resultOperations);

        System.out.print(resultOperations.size());
    }


    private static class Operation implements Comparable<Operation> {
        private int startDay;
        private int endDay;
        private int duration;

        public Operation(int startDay, int duration) {
            this.startDay = startDay;
            this.duration = duration;
            this.endDay = startDay + duration;
        }

        public int getStartDay() {
            return startDay;
        }

        public int getDuration() {
            return duration;
        }

        public int getEndDay() {
            return endDay;
        }

        @Override
        public int compareTo(Operation o) {
            return Integer.compare(this.endDay, o.getEndDay());
        }

        @Override
        public String toString() {
            return "Operation{" +
                    "startDay=" + startDay +
                    ", endDay=" + endDay +
                    ", duration=" + duration +
                    '}';
        }
    }

}
