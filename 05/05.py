with open('./boarding passes.txt') as f:
    boarding_passes = f.read()

boarding_passes = boarding_passes.split('\n')


def get_row(boarding_pass):
    row_string = boarding_pass[0:7]
    row_string = row_string.replace('F', '0')
    row_string = row_string.replace('B', '1')
    row = int(row_string, 2)

    return row


def get_seat(boarding_pass):
    seat_string = boarding_pass[7:]
    seat_string = seat_string.replace('R','1')
    seat_string = seat_string.replace('L','0')

    seat = int(seat_string, 2)

    return seat


def get_seat_id(boarding_pass):
    row = get_row(boarding_pass)
    seat = get_seat(boarding_pass)

    return row * 8 + seat


seat_ids = []

for boarding_pass in boarding_passes:
    seat_ids.append(get_seat_id(boarding_pass))

print(f'Sanity check: {max(seat_ids)}')


def missing_seat(list_of_seats):
    list_of_seats = sorted(list_of_seats)
    start, end = list_of_seats[0], list_of_seats[-1]
    return set(range(start, end + 1)).difference(list_of_seats)


print(f'My seat: {missing_seat(seat_ids)}')
