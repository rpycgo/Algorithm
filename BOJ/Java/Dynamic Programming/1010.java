package boj;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);		
		
		int T = sc.nextInt();
		
		for(int i = 0; i < T; i++) {
			int N = sc.nextInt();
			int M = sc.nextInt();
			
			System.out.println(solution(N, M));
		}
	}
	
	public static int solution(int n, int m) {
		int[][] dp = new int[n][m];
		
		for (int i = 0; i < n; i++) {
			dp[i][i] = 1;
		}
		
		for (int j = 0; j < m; j++) {
			dp[0][j] = j + 1;
		}
		
		if (n >= 2) {
			for (int i = 1; i < n; i++) {
				for (int j = i; j < m; j++) {
					dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1];
				}
			}
		}
	
	return dp[n - 1][m - 1];
	}
}
