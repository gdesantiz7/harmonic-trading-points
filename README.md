# Harmonic Trading Points
The Fibonacci sequence is one of the most famous formulas in mathematics because it is observed throughout nature.  Each number in the sequence is the sum of the two numbers that precede it.  So, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, and so on.  After the eighth sequence of calculations, there are constant mathematical ratio relationships that can be derived from the series.  Starting with the sum of the eighth calculation (34) as the numerator and using the sum of the ninth equation (55) as the denominator, the result yields 0.618.  In the inverse calculation of these numbers, the same rules apply and the calculation yields 1.618.  Interestingly enough, this study can be applied to financial markets in the form of ratios (i.e., 0.618 and 1.618) derived from the Fibonacci sequence.  Harmonic trading is an area of technical analysis that utilizes the powerful synergies of Fibonacci measurement techniques to quantify specific price patterns.

In the Universe...

<img src="images/Screen Shot 2021-02-13 at 2.05.19 PM.png" width="225" height="200">

In Financial Markets...

<img src="images/Screen Shot 2021-02-13 at 2.21.21 PM.png" width="260" height="190">

The primary goal of this project is to provide a harmonic trading function that can distinguish all points within a 5-point price structure given each Fibonacci calculation that corresponds with a specific harmonic pattern.

## Using Harmonic Trading Points
Harmonic trading patterns are comprised of five points X, A, B, C, and D.  In this function, the user must supply the X point (the starting price of the pattern), the A point (the ending price of the first move in the pattern), the XAB ratio (the percentage of the B point relative to points X and A), the ABC ratio (the percentage of the C point relative to points A and B), the BCD ratio (the percentage of the D point relative to points B and C), the XAD ratio (the percentage of the D point relative to points X and A), and the AB=CD ratio (the percentage of the D point relative to points A and B).  The output is a five point harmonic trading pattern or five points in currency terms and a potential reversal zone (PRZ) which encompasses D, XAD, and ABCD.

So in the example we have below, there is a theoretical asset with a starting price of 1460 (represented by X) and then it makes a move up to 1520 (represented by A).  If we wanted to see what the rest of the prices would be at B, C, and D according to a "perfect bat pattern" we would plug in the values of 0.5 (represented by XAB), 0.618 (represented by ABC), 2.0 (represented by BCD), 0.886 (represented by XAD), and 1.27 (represented by ABCD).  All of these parameters would return what is seen below, and if all of the price levels were touched in the "potential reversal zone" then perhaps this could signal a buy.

<img src="images/Screen Shot 2021-02-13 at 3.14.32 PM.png" width="650" height="110">

## Links
* Harmonic Pattern Education: [Harmonic Trader](https://www.harmonictrader.com/)
* Harmonic Pattern Software: [FormationSeeker](https://www.formationseeker.com/)
