def solve():
    # Read N (Highway Length) and M (Number of Projects)
    N, M = list(map(int, input().split()))

    # --- PHASE 1: DIFFERENCE ARRAY FOR UPDATES ---
    # Size N+2 to handle 1-based indexing and the R+1 boundary safely
    diff = [0] * (N + 2)

    for _ in range(M):
        L, R, V = list(map(int, input().split()))
        # Mark increase and decrease of value segments
        diff[L] += V
        if R + 1 <= N:
            diff[R + 1] -= V

    # --- PHASE 2: RECONSTRUCTION & PREFIX SUMS ---
    # We need to compute the actual values of the sections and build prefix sum array.
    prefix_sums = [0] * (N + 1)
    current_scenic_value = 0

    for i in range(1, N + 1):
        # Reconstruct the value at section i
        current_scenic_value += diff[i]
        # Add to prefix sum
        prefix_sums[i] = prefix_sums[i-1] + current_scenic_value

    # Helper to get sum in O(1)
    def get_sum(L, R):
        if L > R:
            return None
        return prefix_sums[R] - prefix_sums[L-1]

    # --- PHASE 3: TRAFFIC SCENARIOS ---
    Q = int(input())

    for _ in range(Q):
        accidents = list(map(int, input().split()))

        '''User forgets to sort accidents causing wrong values'''
        # accidents.sort()

        # Add "Virtual Barriers" at 0 (start) and N+1 (end)
        # A valid drive is the space between two barriers.
        barriers = [0] + accidents + [N + 1]

        max_trip_value = -float('inf')
        driveable = False

        # Check every segment between barriers
        for i in range(1, len(barriers)):
            # The segment starts one section after the previous barrier
            # and ends one section before the current barrier
            seg_start = barriers[i-1] + 1
            seg_end = barriers[i] - 1

            current_trip_value = get_sum(seg_start, seg_end)
            # Ensure it's a valid range
            if current_trip_value is None:
                continue

            driveable = True
            if current_trip_value > max_trip_value:
                max_trip_value = current_trip_value

        if driveable:
            print(max_trip_value)
        else:
            print("Impossible")

if __name__ == "__main__":
    solve()
