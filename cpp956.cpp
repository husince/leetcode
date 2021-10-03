class Solution {
public:
  int tallestBillboard(vector<int>& rods) {    
    const int s = accumulate(begin(rods), end(rods), 0);
    vector<int> dp(s + 1, -1);    
    dp[0] = 0;
    for (int rod : rods) {    
      vector<int> cur(dp);
      for (int i = 0; i <= s - rod; ++i) {
        if (cur[i] < 0) continue;
        dp[i + rod] = max(dp[i + rod], cur[i]);
        dp[abs(i - rod)] = max(dp[abs(i - rod)], cur[i] + min(rod, i));
      }    
    }
    return dp[0];
  }
};