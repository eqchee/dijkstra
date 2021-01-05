# Dijkstra's Algorithm 



## About The Project

In a country with multiple towns connected by numerous bidirectional roads, only a few towns  have a voting station. Each citizen would start with a green card to allow them to travel and they would like to travel to a voting station in minimal time. Each time a citizen travels from one town to another and if the two towns are hostile, the green card would be downgraded to orange card, or the orange card would be downgraded to red card. To upgrade from a red card to orange card or from orange card to green card, each city would have their own processing time. If the two towns are friendly, there is no change to the card.  It is only possible to travel with a green or orange card. If a citizen receives a red card, he/she must upgrade his/her card to either orange or green before being able to leave for the next town. To enter the voting station, the citizen must have a green card.

This algorithm has been designed to determine the path with minimum travelling time required to reach a voting station from each town in the country by modifying Dijkstra's algorithm:

1.  Set towns with voting station to be sources, ie. cost to be 0
2. For each town (vertex), split it into 3 sub-vertices to account for all possible permutations of card downgrade/upgrade(s)

