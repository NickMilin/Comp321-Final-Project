import java.util.*;

public class TheScenicRoute {

    private static void scenicRouteSolution() {

        Scanner scanner = new Scanner(System.in); // Scanner to read from standard input

        int N = scanner.nextInt(); // Length of the highway (number of segments)
        int M = scanner.nextInt(); // Number of beautification projects

        // Difference array for efficient range updates
        int[] diff = new int[N + 2]; // +2 to safely handle diff[R+1]

        // Apply each beautification project using range updates
        for (int i = 0; i < M; i++) {
            int L = scanner.nextInt(); // Start index of project
            int R = scanner.nextInt(); // End index (inclusive)
            int V = scanner.nextInt(); // Scenic value change

            diff[L] += V;      // Start applying V at L
            diff[R + 1] -= V;  // End applying V after R
        }

        // Build actual scenic values from diff[]
        int[] scenic = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            diff[i] += diff[i - 1];
            scenic[i] = diff[i];
        }

        // Build prefix sum array of scenic values
        int[] prefix = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            prefix[i] = prefix[i - 1] + scenic[i];
        }

        int Q = scanner.nextInt(); // Number of traffic scenarios
        scanner.nextLine();        // Consume leftover newline

        // Process each traffic scenario
        for (int q = 0; q < Q; q++) {

            // Safe accident line reading
            String line = "";

            // First attempt to read a line only if one exists
            if (scanner.hasNextLine()) {
                line = scanner.nextLine().trim();
            }

            // Skip empty lines *but only if there are more lines available*
            while (line.isEmpty() && scanner.hasNextLine()) {
                line = scanner.nextLine().trim();
            }

            // If line is empty here, it means:
            // - There were no accident locations
            // - The entire highway has no blocked segments
            if (line.isEmpty()) {
                int fullSum = prefix[N];  // sum of entire highway
                System.out.println(fullSum);
                continue; // Move to next scenario
            }

            // Parse accidents
            String[] parts = line.split(" ");  // Split accident positions
            int[] accidents = new int[parts.length];

            for (int i = 0; i < parts.length; i++) {
                accidents[i] = Integer.parseInt(parts[i]);
            }

            Arrays.sort(accidents); // Sort so we process segments left→right

            int best = Integer.MIN_VALUE; // Best scenic segment found
            int prev = 1;                 // Start of current valid stretch

            // For each accident, compute scenic sum before it
            for (int acc : accidents) {
                int L = prev;
                int R = acc - 1; // Segment stops right before accident

                if (L <= R) {
                    int sum = prefix[R] - prefix[L - 1];
                    best = Math.max(best, sum);
                }

                prev = acc + 1; // Next segment starts AFTER accident
            }

            // After the last accident, check the remaining segment
            if (prev <= N) {
                int sum = prefix[N] - prefix[prev - 1];
                best = Math.max(best, sum);
            }

            // Output result
            if (best == Integer.MIN_VALUE) {
                System.out.println("Impossible");
            } else {
                System.out.println(best);
            }
        }

        scanner.close();
    }

    public static void main(String[] args) {
        scenicRouteSolution();
    }
}
