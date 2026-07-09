class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        min_overall_finish_time = math.inf

        lr = []
        wr = []
        for i in range(len(landStartTime)):
            lr[i] = landStartTime[i] + landDuration[i]

        for i in range(len(waterStartTime)):
            wr[i] = waterStartTime[i] + waterDuration[i]

        
        return int(min_overall_finish_time)
