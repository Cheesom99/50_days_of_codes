# BIRTHDAY SPEED TICKET, <60 for no ticket, 60<x<80 for low ticket, >80 for a big ticket
def birthday_ticket(is_birthday, speed):
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    if speeding > 80:
        print('Big Ticket')
    elif 60 < speeding < 80:
        print('Small Ticket')
    else:
        print('No ticket')


birthday_ticket(True, 82)
