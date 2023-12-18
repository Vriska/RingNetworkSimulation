# RingNetworkSimulation

This is a simulation of a hypothetical improvement to the outdated IBMs Token Ring system simulated under the assumtion that there is going to be heavy traffic under some nodes
and the weight and intensity around that node is going to be normally distributed ie -there is a lot of traffic around certain servers of the ring. This simulation method shows in 
such cases, wait time and other metrics are optimized if the token was randomized in motion between servers rather than completeing the entire ring which leads to a notable 
increase in wait time due to having to go an highly active section of the ring before first .

# Factored Highest Response Ratio Scheduler


The Response Ratio is W+S/S were W is weight time and S is burst Time, the Highest Response Ratio scheduler prioritizes tasks by response ratio, but what if a factor
was introduced such that F*W+S/S where F is the factor. As F increases the significance of weight time increases slowly make it in essence a first come first serve system
with large enough F, but as F is made smaller the priority goes to the largest tasts first. This code is intended to test various F under different conditions so an optimal
may be chosen given a particular set of tasks . F may also be changed dynamically to find optimized scheduling if data aligns, but this increases scheduling overhead
