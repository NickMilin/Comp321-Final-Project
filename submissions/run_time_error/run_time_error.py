def solve():
    # Read N (Highway Length) and M (Number of Projects)
    N, M = list(map(int, input().split()))

    # --- PHASE 1: DIFFERENCE ARRAY FOR UPDATES ---
    '''Forgets sections are indexed-1'''
    '''Makes difference array N+1 size instead of N+2'''
    diff = [0] * (N + 1)

    for _ in range(M):
        L, R, V = list(map(int, input().split()))
        # Mark increase and decrease of value segments
        diff[L] += V
        diff[R + 1] -= V

    print(diff)

    # --- PHASE 2: RECONSTRUCTION & PREFIX SUMS ---
    '''Makes prefix sums array N size instead of N+1'''
    prefix_sums = [0] * N
    current_scenic_value = 0

    for i in range(1, N):
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

        # Sort accidents to make getting max values linear
        accidents.sort()

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
