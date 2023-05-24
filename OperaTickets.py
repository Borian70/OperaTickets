operas = []
ticket_counts = {
    "standard": 0,
    "student": 0,
    "pensioner": 0,
    "kid": 0
}

while True:
    opera_name = input()
    if opera_name == "Finish":
        break

    total_seats = int(input())
    seats_sold = 0

    while seats_sold < total_seats:
        ticket_type = input().lower()
        if ticket_type == "end" or ticket_type == "finish":
            break

        ticket_counts[ticket_type] += 1
        seats_sold += 1

    percent_filled = (seats_sold / total_seats) * 100
    operas.append((opera_name, percent_filled))

    if ticket_type == "finish":
        break

total_tickets_sold = sum(ticket_counts.values())

for opera in operas:
    print(f"{opera[0]} - {opera[1]:.2f}% full.")

print(f"Total tickets: {total_tickets_sold}")
for ticket_type, count in ticket_counts.items():
    if count == 0:
        continue

    percent = (count / total_tickets_sold) * 100
    print(f"{percent:.2f}% {ticket_type} tickets")
