package_pens = int(input())
package_markers = int(input())
liters_cleaning = int(input())
percent = int(input())


PACKAGE_PENS_PRICE = 5.80
PACKAGE_MARKERS_PRICE = 7.20
PREPARATION_CLEANING_PRICE = 1.20

sum = package_pens * PACKAGE_PENS_PRICE \
            + package_markers * PACKAGE_MARKERS_PRICE \
            + liters_cleaning * PREPARATION_CLEANING_PRICE

total_sum = sum - (sum*0.25)

print(total_sum)