from collections import deque

class Solution:
    def computeDayGains(self, nbSeats, payingGuests, guestMovements):
        guest_status = {i+1: "out" for i in range(len(payingGuests))} # seated, waiting, or out
        seats = 0
        paid_set = set() #[False for i in range(len(payingGuests))]
        waiting_queue = deque()
        for i, curr_guest in enumerate(guestMovements):
            if guest_status[curr_guest] == "out":
                if seats < nbSeats:
                    guest_status[curr_guest] = "seated"
                    paid_set.add(curr_guest)
                    seats += 1
                else:
                    guest_status[curr_guest] = "waiting"
                    waiting_queue.append(curr_guest)
            elif guest_status[curr_guest] == "waiting":
                guest_status[curr_guest] = "out"
                waiting_queue.remove(curr_guest)
            elif guest_status[curr_guest] == "seated":
                guest_status[curr_guest] = "out"
                seats -= 1
                if len(waiting_queue) > 0:
                    next_seated_guest = waiting_queue.popleft()
                    guest_status[next_seated_guest] = "seated"
                    paid_set.add(next_seated_guest)
                    seats += 1    
        revenue = 0
        for customer in paid_set:
            revenue += payingGuests[customer-1]
        return revenue
    

def main():
    soln = Solution()
    nbSeats = 2
    payingGuests = [1, 7, 4, 6, 9]
    guestMovements = [3, 3, 2, 4, 1, 3, 5, 4, 3, 1]
    # nbSeats = 3
    # payingGuests = [1, 7, 4, 6, 9, 2, 1, 8]
    # guestMovements = [4, 2, 4, 3, 5, 1, 2, 8, 6, 8, 7, 3, 7, 8, 5, 8]
    revenue = soln.computeDayGains(nbSeats, payingGuests, guestMovements)
    print("Daily Revenue:", revenue)
    return 0


if __name__ == "__main__":
    main()
