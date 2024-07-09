# Algebraic-Division-Algorithm
Algebraic division plays a significant role, particularly in factoring and optimizing logic functions represented in Boolean algebra. Here’s how algebraic division is relevant in factoring within Multilevel Synthesis:
1. Factoring for Multilevel Logic Synthesis & Logic Function Optimization:
   - Algebraic division is used to factor these Boolean expressions into simpler forms. This process helps in reducing the complexity of the logic function, which can lead to 
     optimized circuit designs in terms of area, power consumption, and speed.
2. Common Subexpression Elimination:
   - Algebraic division is utilized to identify and eliminate common subexpressions within the logic function. By dividing the original expression by a common factor, the 
     resultant factors can be combined or simplified to reduce the overall number of gates required to implement the circuit. This reduction is crucial in improving the 
     efficiency and performance of the designed digital circuit.
3. Algebraic Manipulation Techniques:
   - Various algebraic manipulation techniques, including algebraic division, are employed in Multilevel Synthesis to transform and optimize Boolean expressions. These 
     techniques often involve transforming complex Boolean functions into more manageable forms, such as sum-of-products (SOP) or product-of-sums (POS) expressions, which are 
     easier to implement using standard logic gates.

# Idea
![](https://github.com/3a3del/Algebraic-Division-Algorithm/blob/main/temp2.PNG)                    

# Algebraic Division: Very Nice Algorithm
- Inputs:
  - A Boolean expression F and a D divisor (to divide by) D, represented as lists of cubes(and each cube a set of literals).
  - The input F text file should be in form like if F = axc + axd + axe + bc + bd + de so...
  - 
![](https://github.com/3a3del/Algebraic-Division-Algorithm/blob/main/temp.PNG)


Also the divisor, D = ax + b..


![](https://github.com/3a3del/Algebraic-Division-Algorithm/blob/main/temp3.PNG)

# Output 
   • Quotient Q = F/D = cubes in quotient, or 0 (empty) if none 
   • Remainder R = cubes in remainder, or 0 (empty) if D was a factor 
   • i.e., figures out Q, R so that F = D•Q+ R = D•(F/D) + R 
   
![](https://github.com/3a3del/Algebraic-Division-Algorithm/blob/main/ouput.PNG)
                        
  
                                        
  
  
