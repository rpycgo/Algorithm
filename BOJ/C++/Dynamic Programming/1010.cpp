#include <iostream>

using namespace std;

template <typename T>
T solution(const T n, const T m) {
	int** dp = new int*[n];
	for (int i = 0; i < n; i++) {
		dp[i] = new int[m];
	}

	for (int i = 0; i < n; i++) {
		dp[i][i] = 1;
	}

	for (int i = 0; i < m; i++) {
		dp[0][i] = i + 1;
	}

	if (n >= 2) {
		for (int i = 1; i < n; i++) {
			for (int j = i; j < m; j++) {
				if (i != j) {
					dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1];
				}
			}
		}
	}

	return dp[n - 1][m - 1];
}

int main() {
	int T, N, M;

	cin >> T;
	
	for (int i = 0; i < T; i++) {
		cin >> N >> M;
		cout << solution(N, M) << endl;
	}
}
