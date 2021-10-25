from air_hockey_env import Air_hockey_env


class Random_game():
	def __init__(self):
		self.xd = Air_hockey_env(60, 30)
		self.xd.reset()
		done = False

		while not done:
			action = self.xd.sample()
			action2 = self.xd.sample()
			state, reward1, reward2, done = self.xd.step(action, action2)

		#print('plox')

	def render(self):
		plox1, plox2 = self.xd.render()
		return plox1, plox2
