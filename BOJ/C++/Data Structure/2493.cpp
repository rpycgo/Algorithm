#include <iostream>
#include <stack>
#include <algorithm>

using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, height;
	stack<pair<int, int>> top;

	top.push({ 100000001, 0 });
	cin >> N;
	for (int i = 1; i <= N; ++i) {
		cin >> height;
		while (top.top().first < height) {
			top.pop();
		}

		cout << top.top().second << ' ';
		top.push({ height, i });
	}
	
	return 0;
}