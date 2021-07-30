:
# Assignment day 3
 
'''
Consider a person is represented by Pi, where i is the index of the following list.
A list shows the person to whom person Pi has given the gift.
 
Consider the below example:
gift_presented_to = [2, 1, 5, 3, 4]
 
This list is giving us the following details:
Person P1 has given gift to person P2
Person P2 has given gift to person P1
Person P3 has given gift to person P5
Person P4 has given gift to person P3
Person P5 has given gift to person P4
 
So for the given list, the list of persons from whom they have received the gift would be 
gift_received_from = [2, 1, 4, 5, 3]
 
i.e.
Person P1 has received gift from person P2
Person P2 has received gift from person P1
Person P3 has received gift from person P4
Person P4 has received gift from person P5
Person P5 has received gift from person P3
 
Your task:
 
Take input for the gift_presented_to[] list and print its respective gift_received_from[] list.
'''


x = input('gift_presented_to: ')
val = [int(i) for i in x.split()]
print(val)

gift_received_from = [2, 1, 4, 5, 3]

for i in range(len(val)):
  print("Person P" + str(val[i])  + " has received gift from Person P" + str(gift_received_from[i]))
  
  


'''
gift_presented_to: 55 62 11 52
[55, 62, 11, 52]
Person P55 has received gift from Person P2
Person P62 has received gift from Person P1
Person P11 has received gift from Person P4
Person P52 has received gift from Person P5
'''
