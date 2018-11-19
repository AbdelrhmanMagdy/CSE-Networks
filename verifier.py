import generator, sys

def verify(packet, g):
    reminder = generator.mod2div(packet, g)
    return True if not int(reminder) else False

if __name__ == "__main__":
	if not len(sys.argv) == 3:
		print('args: packet g')
	else:
		packet = sys.argv[1]
		g = sys.argv[2]
		verification = verify(packet, g)
		print('msg is correct!') if verification else print('wrong msg!')
