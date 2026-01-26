class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        def bfs(start_node):
            dists = [-1] * n
            dists[start_node] = 0

            queue = deque([start_node])
            while queue:
                curr_node = queue.popleft()

                for next_node in adj[curr_node]:
                    if dists[next_node] == -1:
                        dists[next_node] = dists[curr_node] + 1
                        queue.append(next_node)

            return dists

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dx = bfs(x)
        dy = bfs(y)
        dz = bfs(z)

        cnt = 0
        for i in range(n):
            a, b, c = sorted([dx[i], dy[i], dz[i]])

            if a**2 + b**2 == c**2:
                cnt += 1

        return cnt
