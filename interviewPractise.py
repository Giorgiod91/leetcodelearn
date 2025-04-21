def bestSeat(seats):
    soloSeats = set()
    for i in range(1, len(seats) - 1):
        if seats[i] == 0 and seats[i - 1] == 0 and seats[i + 1] == 0:
            soloSeats.add(i)
    return soloSeats


print(bestSeat([1,0,1,0,0,0,1]))