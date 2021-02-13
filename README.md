# Harmonic Trading Points
A vast majority of trading in the foreign exchange market as well as many other markets is  considered high frequency trading (HFT), where transactions are executed by machines, allowing the process to be automated and the calculations to be made at a rapid rate on a great scale.  With this notion in mind, one foreign exchange trade is usually comprised of several other smaller trades all with different notional values and prices.  To determine the total notional value of the base currency position and the average price, a weighted average formula must be  applied.

The primary goal of this project is to provide a basic weighted average function that can not only be used in foreign exchange but also many other asset classes as well.

## Using Harmonic Trading Points
First, import List from the typing library followed by holding shift and pressing enter.

<img src="images/Screen Shot 2019-11-11 at 12.43.27 PM.png" width="210" height="20">

Next, copy and paste the fx_weighted_average function into a cell and again hold shift and press enter.

If you would like to enter a lot over 100, please comment out the entire assert statement in the code block below (enter # next to each line) or change the constant 100 to the desired threshold.

<img src="images/Screen Shot 2019-11-11 at 12.44.52 PM.png" width="550" height="55">

In addition, in currency trading, a lot represents a certain amount of units which in this case is 1,000,000.  If you would like to change the unit size, simply modify the constant value of 1,000,000 in the lots_1_mio local variable.

<img src="images/Screen Shot 2019-11-11 at 12.45.09 PM.png" width="350" height="22">

Lastly, type fx_weighted_average() and within the parenthesis, enter two lists separated by a comma with one representing all the transacted lots and the other with the corresponding prices.  Please note that each lot should be in the same order of the list as its associated price or the weights will be incorrect.

<img src="images/Screen Shot 2019-11-11 at 1.00.08 PM.png" width="400" height="25">

Using the provided example above, the output should look like this: 6,000,000 at 1.11290

## Links
* Harmonic Pattern Education: [Harmonic Trader](https://www.harmonictrader.com/)
* Harmonic Pattern Software: [FormationSeeker](https://www.formationseeker.com/)
