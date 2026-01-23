#include <iostream>
#include <vector>

using namespace std;


void dfs(
    int curr_node, vector<bool>& visited,
    vector<vector<int>>& dp, vector<vector<int>>& adj) {
    visited[curr_node] = true;

    for (int neighbor_node : adj[curr_node]) {
        if (!visited[neighbor_node]) {
            dfs(neighbor_node, visited, dp, adj);

            dp[curr_node][0] += dp[neighbor_node][1];
            dp[curr_node][1] += min(dp[neighbor_node][0], dp[neighbor_node][1]);
        }
    }
}


int main() {
    int N, u, v;
    cin >> N;
    
    vector<vector<int>> adj(N+1);
    for (int i = 0; i < N-1; i++){
        cin >> u >> v;

        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<bool> visited(N+1, false);

    vector<vector<int>> dp(N+1, vector<int>(2));
    for (int i = 1; i <= N; i++){
        dp[i][0] = 0;
        dp[i][1] = 1;
    }

    dfs(1, visited, dp, adj);

    cout << min(dp[1][0], dp[1][1]);
}