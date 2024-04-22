#Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy.
#What is the total wholesale cost for 60 copies?


#Constants 

cover_price = 24.95 #Cover price of the book
discount_rate = 0.40 #40% discount rate for bookstores
shipping_cost_first_copy = 3.00 #Shipping cost for the first copy
shipping_cost_additional_copy = 0.75 #Shipping cost for each additional copy
num_copies = 60 #Number of copies to order

#Calculation of discounted price pper book after applying the discount rate
discounted_price = cover_price - (discount_rate * cover_price)

#Calculation of the total cost of all books 
total_cost_books = discounted_price * num_copies

#Calculating the total shipping cost by adding the cost by adding the cost for the first copy and the cost for the additional copies
total_shipping_cost = shipping_cost_first_copy + (num_copies - 1) * shipping_cost_additional_copy

#Calculating the total wholesale cost by adding the total cost of books and the total shipping cost
total_wholesale_cost = total_cost_books + total_shipping_cost

#Printing the total wholesale cost

print("Total Wholesale Cost for 60 Copies: $", total_wholesale_cost)