class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> solutions;

        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1;
            int right = nums.size() - 1;

            while (left < right) {
                int s = nums[i] + nums[left] + nums[right];
                if (s > 0) right--;
                else if (s < 0) left++;
                else {
                    vector<int> sol = {nums[i], nums[left], nums[right]};
                    solutions.push_back(sol);
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                }
                //cout << left << " " << right << endl;
            }
        }

        return solutions;
    }
};