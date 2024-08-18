class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        total_moves = 0
        seats.sort()
        students.sort()
        for seat, student in zip(seats,students):
            total_moves = total_moves + abs(seat-student)
        return total_moves