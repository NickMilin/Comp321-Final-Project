#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Read N (Highway Length) and M (Number of Projects)
    int N, M;
    if (! (cin >> N >> M)) {
        return 0;
    }

    // Difference array for updates
    vector<long long> diff(N + 2, 0);

    // For each project, update the scenic values
    for (int i = 0; i < M; ++i) {
        // Get each project (one per line)
        int L, R;
        long long V;
        cin >> L >> R >> V;

        // Update scenic values
        diff[L] += V;
        if (R + 1 <= N) {
            diff[R + 1] -= V;
        }
    }

    // Reconstruction and prefix sums
    vector<long long> prefix_sums(N + 1, 0);
    long long current_scenic_value = 0;
    for (int i = 1; i <= N; ++i) {
        current_scenic_value += diff[i];
        prefix_sums[i] = prefix_sums[i - 1] + current_scenic_value;
    }

    // Helper to get sum in O(1)
    auto get_sum = [&](int L, int R, long long& out) -> bool {
        if (L > R) {
            return false;
        }
        out = prefix_sums[R] - prefix_sums[L - 1];
        return true;
    };

    // Traffic scenarios
    int Q;
    cin >> Q;
    string line;
    getline(cin, line); // consume trailing newline

    for (int qi = 0; qi < Q; ++qi) {
        getline(cin, line);

        vector<int> accidents;
        if (! line.empty()) {
            stringstream ss(line);
            int val;
            while (ss >> val) {
                accidents.push_back(val);
            }
        }

        // Sort accidents to make getting max values linear
        sort(accidents.begin(), accidents.end());
        // Add "Virtual Barriers" at 0(start) and N + 1(end)
        vector<int> barriers;
        barriers.reserve(accidents.size() + 2);
        barriers.push_back(0);
        barriers.insert(barriers.end(), accidents.begin(), accidents.end());
        barriers.push_back(N + 1);

        long long max_trip_value = numeric_limits<long long>::min();
        bool driveable = false;

        // Check every segment between barriers
        for (size_t i = 1; i < barriers.size(); ++i) {
            int seg_start = barriers[i - 1] + 1;
            int seg_end = barriers[i] - 1;

            seg_start = max(seg_start, 1);
            seg_end = min(seg_end, N);

            long long current_trip_value = 0;
            if (! get_sum(seg_start, seg_end, current_trip_value)) {
                continue;
            }

            driveable = true;
            if (current_trip_value > max_trip_value) {
                max_trip_value = current_trip_value;
            }
        }

        if (driveable) {
            cout << max_trip_value << '\n';
        }
        else {
            cout << "Impossible\n";
        }
    }

    return 0;
}
