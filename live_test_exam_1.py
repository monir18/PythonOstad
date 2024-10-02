def calculate_ticket_price(age, showtime):
    # Age validation
    if age <= 0:
        return "Invalid input. Age must be a positive integer."

    # Showtime validation (24-hour format)
    if showtime < 0 or showtime >= 2400 or showtime % 100 >= 60:
        return "Invalid input. Please provide the showtime in the correct format."

    # Ticket price based on age
    if age <= 10:
        ticket_price = 300
    elif 11 <= age <= 25:
        ticket_price = 500
    elif 26 <= age <= 60:
        ticket_price = 800
    else:
        ticket_price = 400

    # Check for discount (if showtime is before 1700)
    discount = 0
    if showtime < 1700:
        discount = ticket_price * 0.10

    discounted_price = ticket_price - discount

    # Return ticket price and discount details
    return (f"Ticket price: {ticket_price} BDT\n"
            f"Discount: {discount:.2f} BDT\n"
            f"Discounted price: {discounted_price:.2f} BDT")


try:
    age = int(input("Age: "))
    showtime = int(input("Showtime (HHMM): "))

    result = calculate_ticket_price(age, showtime)
    print(result)

except ValueError:
    print("Invalid input. Please enter valid age and showtime.")
