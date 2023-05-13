from typing import Optional
from typing import Tuple
from FourRooms import FourRooms
import numpy as np

class RLAgent:
	def __init__(self) -> None:
		self.room: Optional[FourRooms] = None

	def set_room(self, room: FourRooms):
		self.room = room

	def get_next_move(self):
		return np.random.randint(low=0, high=4)
	
	def move(self, move: int) -> Tuple[int, Tuple[int, int], int, bool]:
		return self.room.takeAction(move) # type: ignore