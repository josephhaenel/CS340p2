JOSEPH HAENEL 4/6/2023

cd into CS340p2, run file with py main.py. BST is based off of a previous implementation of BST in c++ that I had made and translated to python with help from the books provided code.
R-B is using the books provided code and a lot of tears.


Bullet-point 1: "Provide examples of queries that are fast, and queries that are slow.  
Show actual running times for various queries.  Describe why query performance is behaving as it is in these cases."

A creation of a Sorted Set of 150k words is considerably slow because the execution time is proportionate to the 
height/depth of the tree. And in a BST of Sorted inputs, the tree will be n height/depth.
This is because the graph is extremely one sided due to the first input being the biggest or smallest value in the tree,
and every value after that will be bigger or smaller respectively. Causing a tree to be a line of nodes.

Ex. BST - 150k Sorted Time: 1226.124s vs 150k Permuted Time: 1.041s

Whereas, the creation of a Permuted Set of 150k words is considerably faster because the depth/height is proportionally 
less than the sorted tree. This is because the tree is likely not as one sided, (though likely not a balanced tree)
, causing the creation to be much faster.


In the R-B tree however, the creation of a Permuted list of 150k words and a Sorted list of 150k words is relatively similar.
This is due to the fact that R-B trees are always balanced, and even with a sorted list of inputted values, the R-B tree is
still able to maintain a balanced tree. The only thing slowing down the creation in the sorted tree is likely the 
significant amount of extra work it is having to do with left and right shifts to stay balanced.
Ex. R-B - 150k Sorted Time: 0.6083s  vs 150k Permuted Time: 0.4477s



Bullet-point 2: "From the plots: Graph the execution time of constructing your BST and Red-Black Tree as a function of size (number of words), 
and discuss if your plots behave as expected given Big-Oh function behavior."

BST:
    SORTED: In the worst case, such as a sorted list of inputted words, BST time complexity is n^2, which is apparent in the graph where Sorted is exponentially increasing.
        So, the expected worst case is behaving as expected.
    PERMUTED: In the average/best case, such as a random list of inputted words, BST time complexity is n(logn), which is somewhat apparent, though hard to visualize for humans, in the graph.
        So, the expected average/best case is behaving as expected.
R-B:
    For both sorted and permuted cases, the average/expected creation time is n(logn), which is apparent in the graph. The only difference is the addition of the amount of time
    shifting is adding for the Sorted input, which is the worst case, but still results in a balanced tree. You can see the same relative trendline in the graph. 
    So, the expected behavior can be observed by the R-B tree in permuted and sorted cases.