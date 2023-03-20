number_of_people = int(input())
number_of_night = int(input())
number_of_cards_for_transport = int(input())
number_of_tickets_for_museum = int(input())


Night = 20
Card = 1.60
Ticket = 6
percent_1 = 0.25

for_one_person = number_of_night * Night + number_of_cards_for_transport * Card + number_of_tickets_for_museum  * Ticket
total_sum = for_one_person * number_of_people
total_price = total_sum * percent_1 + total_sum



print(f"{total_price:.2f}")
