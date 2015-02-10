if self.find_trend(prev, val, NON_DECREASING):
                positive_trend += 1
            else:
                self.positive_deque.append(Node(i-positive_trend, i, NON_DECREASING))
                positive_sum += summation(positive_trend)
                positive_trend = 1
            if self.find_trend(prev, val, NON_INCREASING):
                negative_trend += 1
            else:
 
                self.negative_deque.append(Node(i-negative_trend, i, NON_INCREASING))
                negative_sum += summation(negative_trend)
                negative_trend = 1