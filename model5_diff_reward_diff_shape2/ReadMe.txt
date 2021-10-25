Zmiana zwracanych rewardow (nie nagradzamy za zdobycie punktu a punishujemy za strate)	

		if self.ball.y == 1:
			reward2 -= 10
			self.points1 += 1

		elif self.ball.y == self.Y-2:
			reward1 -= 10


oraz nie podawanie agentom do statu pozycji paletki przeciwnika

oraz za +1 point za zdobycie punktu