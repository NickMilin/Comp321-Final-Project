import time

def solve():
    # start_time = time.perf_counter()

    # Read N (Highway Length) and M (Number of Projects)
    N, M = list(map(int, input().split()))

    # --- PHASE 1: BEAUTIFICATION UPDATES ---
    '''Create a list of scenic values and update list directly'''
    scenic_values = [0] * (N + 1)

    for j in range(M):
        L, R, V = list(map(int, input().split()))
        # Mark increase and decrease of value segments
        for i in range(L, R+1):
            scenic_values[i] += V

    # --- PHASE 2: TRAFFIC SCENARIOS ---
    Q = int(input())

    for _ in range(Q):
        accidents = list(map(int, input().split()))
        
        # Sort accidents
        accidents.sort()
        
        # Add "Virtual Barriers" at 0 (start) and N+1 (end)
        barriers = [0] + accidents + [N + 1]
        
        max_trip_value = -float('inf')
        driveable = False

        # Check every segment between barriers
        for i in range(1, len(barriers)):
            # The segment starts one section after the previous barrier
            # and ends one section before the current barrier
            seg_start = barriers[i-1] + 1
            seg_end = barriers[i]

            '''Create a new array of segments and calculates the sum directly'''
            segment = scenic_values[seg_start:seg_end]
            current_trip_value = sum(segment)

            # print(current_trip_value)
            if current_trip_value != 0:
                driveable = True

            if current_trip_value > max_trip_value:
                max_trip_value = current_trip_value
        
        if driveable:
            print(max_trip_value)
        else:
            print("Impossible")

    # end_time = time.perf_counter()
    # print(f"Time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    solve()
