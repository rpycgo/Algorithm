class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        segments = []
        start = 0

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                segments.append((start, i - 1))
                start = i
        segments.append((start, n - 1))

        prefix_counts = []
        total = 0
        for s, e in segments:
            length = e - s + 1
            count = length * (length + 1) // 2
            total += count
            prefix_counts.append(total)

        answer = []
        for l, r in queries:
            left_idx = self.bisect(segments, l) - 1
            right_idx = self.bisect(segments, r) - 1

            if left_idx < 0:
                left_idx = 0
            if right_idx < 0:
                right_idx = 0

            if left_idx == right_idx:
                seg_start, seg_end = segments[left_idx]
                length = r - l + 1
                count = length * (length + 1) // 2
                answer.append(count)
            else:
                seg_start, seg_end = segments[left_idx]
                left_length = seg_end - l + 1
                left_count = left_length * (left_length + 1) // 2

                seg_start_r, seg_end_r = segments[right_idx]
                right_length = r - seg_start_r + 1
                right_count = right_length * (right_length + 1) // 2

                mid_count = 0
                if right_idx - left_idx > 1:
                    mid_count = prefix_counts[right_idx - 1] - prefix_counts[left_idx]

                answer.append(left_count + mid_count + right_count)

        return answer

    def bisect(self, segments, x):
        low, high = 0, len(segments)

        while low < high:
            mid = (low + high) // 2

            if segments[mid][0] <= x:
                low = mid + 1
            else:
                high = mid

        return low
