from board import Board
from copy import deepcopy

class AI:
	def __init__(self, color):
		self.color = color
	
	def minimax(self, current_board, is_maximizing, depth, turn):
		# Tries to find recursively the best value depending on which player is passed as an argument to the function
		if depth == 0 or current_board.has_winner():
			return self.get_value(current_board)
		
		next_turn = 'B' if turn == 'W' else 'W'
		board_color_up = current_board.get_color_up()
		current_pieces = current_board.get_pieces()
		piece_moves = list(map(lambda piece: piece.get_moves(current_board) if piece.get_color() == turn else False, current_pieces))

		if is_maximizing:
			maximum = -999
			for index, moves in enumerate(piece_moves):
				if moves == False:
					continue

				for move in moves:
					aux_board = Board(deepcopy(current_pieces), board_color_up)
					aux_board.move_piece(index, int(move["position"]))
					maximum = max(self.minimax(aux_board, False, depth - 1, next_turn), maximum)
				
			return maximum
		else:
			minimum = 999
			for index, moves in enumerate(piece_moves):
				if moves == False:
					continue

				for move in moves:
					aux_board = Board(deepcopy(current_pieces), board_color_up)
					aux_board.move_piece(index, int(move["position"]))
					minimum = min(self.minimax(aux_board, True, depth - 1, next_turn), minimum)
				
			return minimum
	
	def get_move(self, current_board):
		board_color_up = current_board.get_color_up()
		current_pieces = current_board.get_pieces()
		next_turn = "W" if self.color == "B" else "B"
		player_pieces = list(map(lambda piece: piece if piece.get_color() == self.color else False, current_pieces))
		possible_moves = []
		move_scores = []

		for index, piece in enumerate(player_pieces):
			if piece == False:
				continue
			
			for move in piece.get_moves(current_board):
				possible_moves.append({"piece": index, "move": move})
		
		jump_moves = list(filter(lambda move: move["move"]["eats_piece"] == True, possible_moves))

		if len(jump_moves) != 0:
			possible_moves = jump_moves

		for move in possible_moves:
			aux_board = Board(deepcopy(current_pieces), board_color_up)
			aux_board.move_piece(move["piece"], int(move["move"]["position"]))
			move_scores.append(self.minimax(aux_board, False, 5, next_turn))

		best_score = max(*move_scores)
		best_moves = []

		for index, move in enumerate(possible_moves):
			if move_scores[index] == best_score:
				best_moves.append(move)
		
		# TODO: randomize
		return {"position_to": best_moves[0]["move"]["position"], "position_from": player_pieces[best_moves[0]["piece"]].get_position()}
	

	def get_value(self, board):
		board_pieces = board.get_pieces()

		if board.has_winner():
			if board_pieces[0].get_color() == self.color:
				return 2
			else:
				return -2
		
		total_pieces = len(board_pieces)
		player_pieces = len(list(filter(lambda piece: piece.get_color() == self.color, board_pieces)))
		opponent_pieces = total_pieces - player_pieces

		if player_pieces == opponent_pieces:
			return 0
		
		return 1 if player_pieces > opponent_pieces else -1