#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N; cin >> N;
    vector<int> A(N), B(N), C(N), D(N);

    for (int i = 0; i < N; i++)
        cin >> A[i] >> B[i] >> C[i] >> D[i];

    vector<int> AB, CD;
    AB.reserve(N * N);
    CD.reserve(N * N);

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) {
            AB.push_back(A[i] + B[j]);
            CD.push_back(C[i] + D[j]);
        }

    sort(CD.begin(), CD.end());

    long long answer = 0;
    for (int val : AB) {
        auto range = equal_range(CD.begin(), CD.end(), -val);
        answer += distance(range.first, range.second);
    }

    cout << answer << "\n";

    return 0;
}
