#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <vector>
#include <stdio.h>

using namespace std;

class Maze 
{
private:
	int N, M;
	int** maze, **cnt;
	bool** visited;
	int dx[4] = { 0, 1, 0, -1 };
	int dy[4] = { 1, 0, -1, 0 };
	queue<pair<int, int>> q;

public:
	Maze(const int n, const int m) : N(n), M(m)
	{
		this->maze = new int* [N];
		for (int i = 0; i < N; i++) {
			this->maze[i] = new int[M];
		}

		this->cnt = new int* [N];
		for (int i = 0; i < N; i++) {
			this->cnt[i] = new int[M];
		}

		this->visited = new bool* [N];
		for (int i = 0; i < N; i++) {
			this->visited[i] = new bool[M];
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				this->maze[i][j] = 0;
				this->cnt[i][j] = 0;
				this->visited[i][j] = 0;
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				scanf("%1d", &this->maze[i][j]);
			}
		}
	}

	int bfs(const int x, const int y) {
		this->visited[x][y] = true;
		this->cnt[x][y]++;
		
		this->q.push({ x, y });

		while (!this->q.empty()) {
			int current_x = this->q.front().first;
			int current_y = this->q.front().second;
			this->q.pop();

			for (int i = 0; i < 4; i++) {
				int next_x = current_x + this->dx[i];
				int next_y = current_y + this->dy[i];

				if ((next_x >= 0) && (next_x < N) && (next_y >= 0) && (next_y < M) && (!this->visited[next_x][next_y]) && (this->maze[next_x][next_y] == 1)) {
					this->visited[next_x][next_y] = true;
					this->q.push({ next_x, next_y });
					this->cnt[next_x][next_y] = this->cnt[current_x][current_y] + 1;
				}
			}
		}

		return this->cnt[this->N - 1][this->M - 1];
	}
};


int main() {
	int N, M;
	cin >> N >> M;
	
	Maze maze = Maze(N, M);
	cout << maze.bfs(0, 0) << endl;
}
