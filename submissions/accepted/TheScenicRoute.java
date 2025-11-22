import java.util.*;

public class TheScenicRoute {

    private static void scenicRouteSolution() {

        Scanner scanner = new Scanner(System.in); // Scanner to read input

        int N = scanner.nextInt(); // Length of the highway (number of segments)
        int M = scanner.nextInt(); // Number of beautification projects

        // Difference array for efficient range updates
        // diff[i] will store the change to scenic value at index i
        int[] diff = new int[N + 2]; // +2 to safely handle diff[R+1] update

        // Apply each beautification project
        // Each project increases or decreases the scenic value in a range [L, R]
        for (int i = 0; i < M; i++) {
            int L = scanner.nextInt(); // Start of project (1-indexed)
            int R = scanner.nextInt(); // End of project (1-indexed, inclusive)
            int V = scanner.nextInt(); // Scenic value change (+/-)

            diff[L] += V;       // Add V at the start index
            diff[R + 1] -= V;   // Subtract V after the end index
            // This ensures that when we take prefix sums, the change is applied only to [L,R]
        }

        // Build actual scenic values along the highway
        int[] scenic = new int[N + 1]; // scenic[i] = total scenic value at segment i
        for (int i = 1; i <= N; i++) {
            diff[i] += diff[i - 1]; // Apply the difference array prefix sum
            scenic[i] = diff[i];    // Store actual scenic value
        }

        // Build prefix sum array for fast segment sum queries
        int[] prefix = new int[N + 1]; // prefix[i] = sum of scenic values from 1 to i
        for (int i = 1; i <= N; i++) {
            prefix[i] = prefix[i - 1] + scenic[i];
        }

        int Q = scanner.nextInt(); // Number of traffic scenarios (queries)
        scanner.nextLine();        // Consume leftover newline

        // Process each traffic scenario
        for (int q = 0; q < Q; q++) {
            String line = scanner.nextLine().trim(); // Read a line of accident locations
            while (line.isEmpty()) { // Skip empty lines
                line = scanner.nextLine().trim();
            }

            String[] parts = line.split(" "); // Split by spaces
            int[] accidents = new int[parts.length]; // Array to store accident positions

            for (int i = 0; i < parts.length; i++) {
                accidents[i] = Integer.parseInt(parts[i]); // Convert each to int
            }

            Arrays.sort(accidents); // Sort accidents to process segments in order

            int best = Integer.MIN_VALUE; // Will store the maximum scenic sum without accidents
            int prev = 1; // Start of the current segment (initially the beginning of highway)

            // Loop through accidents to check segments between them
            for (int acc : accidents) {
                int L = prev; // Start of current safe segment
                int R = acc - 1; // End of current safe segment (just before accident)

                if (L <= R) { // If segment exists
                    int sum = prefix[R] - prefix[L - 1]; // Sum of scenic values in this segment
                    best = Math.max(best, sum); // Update maximum scenic sum
                }

                prev = acc + 1; // Move start of next segment to just after this accident
            }

            // Check the segment after the last accident
            if (prev <= N) {
                int sum = prefix[N] - prefix[prev - 1]; // Sum from prev to end
                best = Math.max(best, sum);
            }

            // Output result
            if (best == Integer.MIN_VALUE) {
                System.out.println("Impossible"); // No valid segment
            } else {
                System.out.println(best); // Maximum scenic sum
            }
        }

        scanner.close(); // Close the scanner
    }

    public static void main(String[] args) {
        scenicRouteSolution();
    }
}
