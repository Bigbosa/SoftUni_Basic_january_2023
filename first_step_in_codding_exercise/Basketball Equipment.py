basketball_for_one_year = int(input())

shoes = basketball_for_one_year - basketball_for_one_year * 0.40
basketball_clothes = shoes - shoes * 0.20
basketball_ball = basketball_clothes / 4
basketball_accessories = basketball_ball / 5

full_price = basketball_for_one_year \
             + shoes \
             + basketball_clothes \
             + basketball_ball \
             + basketball_accessories
print(full_price)


