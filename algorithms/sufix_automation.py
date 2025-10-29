class SuffixAutomatonNode:
	def __init__(self):
		self.next = {} # Transition to next states based on character
		self.length = 0 # Length of the node's substring
		self.link = -1 # Suffix link to another state


class SuffixAutomaton:
	def __init__(self):
		self.suffix_automaton = []
		self.last = 0 # Index of the last state in the automaton

	# Initialize the suffix automaton
	def initialize(self):
		initial_node = SuffixAutomatonNode()
		self.suffix_automaton = [initial_node]
		self.last = 0

	# Extend the automaton with a new character
	def extend_automaton(self, c):
		new_node = SuffixAutomatonNode()
		new_node.length = self.suffix_automaton[self.last].length + 1

		current = self.last
		while current != -1 and c not in self.suffix_automaton[current].next:
			self.suffix_automaton[current].next = len(self.suffix_automaton) # Create a new state
			current = self.suffix_automaton[current].link

		if current == -1:
			new_node.link = 0 # The root state
		else:
			next_state = self.suffix_automaton[current].next
			if self.suffix_automaton[current].length + 1 == self.suffix_automaton[next_state].length:
				new_node.link = next_state
			else:
				clone_node = SuffixAutomatonNode()
				clone_node = self.suffix_automaton[next_state]
				clone_node.length = self.suffix_automaton[current].length + 1

				self.suffix_automaton.append(clone_node) # Clone the state

				while current != -1 and self.suffix_automaton[current].next == next_state:
					self.suffix_automaton[current].next = len(self.suffix_automaton) - 1
					current = self.suffix_automaton[current].link

				new_node.link = len(self.suffix_automaton) - 1
				self.suffix_automaton[next_state].link = new_node.link

		self.suffix_automaton.append(new_node)
		self.last = len(self.suffix_automaton) - 1

	# Traverse the suffix automaton
	def traverse_automaton(self):
		print("Traversing Suffix Automaton:")
		for i, state in enumerate(self.suffix_automaton):
			print(f"State {i}, Length: {state.length}, Suffix Link: {state.link}")
			for char, next_state in state.next.items():
				print(f" Transition on '{char}' to State {next_state}")


# Main function
def main():
	input_str = "abab"
	suffix_automaton_instance = SuffixAutomaton()
	suffix_automaton_instance.initialize()

	for char in input_str:
		suffix_automaton_instance.extend_automaton(char)

	# Traverse the constructed suffix automaton
	suffix_automaton_instance.traverse_automaton()


if __name__ == "__main__":
	main()
