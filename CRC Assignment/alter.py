import sys

def alter(packet, i):
    p = list(packet)
    if p[i] == '0':
        p[i] = '1' 
    else:
        p[i] = '0'
    return ''.join(p)

if __name__ == "__main__":
	if not len(sys.argv) == 3:
		print('args: packet index')
	elif int(sys.argv[2]) >= len(sys.argv[1]):
		print('index out of range!')
	else:
		packet = sys.argv[1]
		index = int(sys.argv[2])
		alter_packet = alter(packet, index)
		print(alter_packet)	