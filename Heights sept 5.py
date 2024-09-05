import statistics

heights = [62.5, 68, 70, 71, 71, 72, 73, 73, 74]

mean = statistics.mean(heights)
median = statistics.median(heights)
mode = statistics.multimode(heights)

print(f"The mean of the heights is {mean}\nThe median of the heights is {median}\nFinally the mode of the heights is {mode}")