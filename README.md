# Steiner-Tree-Problem
This is Assignment 3 of CS6013: Advanced Data Structures and Algorithms [IITH] - Steiner Tree Problem



-------------------------------------------------------------------
# Programming Assignment 3
### Name        : Manan Darji
### Roll Number : ************
### Subject     : Advance Data Structure and Algorithm (CS6013)
### Topic       : Steiner Tree Problem
-------------------------------------------------------------------

### Flow Of Code:
* So first we read graph from input.txt
* After which we take user INPUT which is Stainer Vertices.
* Then we find Complete Graph. [FLOYD_WARSHALL_ALGO]
* Then MST from Complete Graph. [PRIMS_ALGO]
* At last we Map to previous graph using parents list.

   
<br/>
<div style="page-break-after: always"></div>

## Few output Examples 
---
### Ex 1
```
--------------------------------------------------
INPUT MATRIX : 
--------------------------------------------------
[[0. 3. 0. 4. 1.]
 [3. 0. 4. 0. 1.]
 [0. 4. 0. 3. 1.]
 [4. 0. 3. 0. 1.]
 [1. 1. 1. 1. 0.]]
--------------------------------------------------
No Of Vertices In Input Graph :  5
--------------------------------------------------
List all the Steiner vertices (type * to quit):
--------------------------------------------------
5
*
--------------------------------------------------
Neighbors of Vertex 1 : [5]
Neighbors of Vertex 2 : [5]
Neighbors of Vertex 3 : [5]
Neighbors of Vertex 4 : [5]
Neighbors of Vertex 5 : [1, 2, 3, 4]
--------------------------------------------------
```

### Ex 2
```
--------------------------------------------------
INPUT MATRIX : 
--------------------------------------------------
[[0. 3. 0. 4. 1.]
 [3. 0. 4. 0. 1.]
 [0. 4. 0. 3. 1.]
 [4. 0. 3. 0. 1.]
 [1. 1. 1. 1. 0.]]
--------------------------------------------------
No Of Vertices In Input Graph :  5
--------------------------------------------------
List all the Steiner vertices (type * to quit):
--------------------------------------------------
1
2
2
Vertex Already Added In Set
3
4
Only One Required Vertex. So, No Path Calculation Needed.
5
No Required Vertices. So, No Path Calculation Needed.
*
--------------------------------------------------
```

</br>
</br>

<center>
<h1>Thank You</h1>
</center>
