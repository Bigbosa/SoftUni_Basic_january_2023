air_company_name = input()
adult_tickets = int(input())
kids_tickets = int(input())
net_price_adult_tickets = float(input())
fee_services = float(input())

percent_kids_ticket = 0.70
percent_all_ticket = 0.20

kids_ticket = net_price_adult_tickets - net_price_adult_tickets * percent_kids_ticket
adult_ticket = net_price_adult_tickets + fee_services
price_kids_ticket = kids_ticket + fee_services
total_sum = adult_tickets * adult_ticket + price_kids_ticket * kids_tickets

profit = "{:.2f}".format(total_sum * percent_all_ticket)

print(f"The profit of your agency from {air_company_name} tickets is {profit} lv.")