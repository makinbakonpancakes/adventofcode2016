from screen import Screen

screen = Screen(6, 50)
instructions = [x.strip('\n') for x in open('input.txt')]
for instr in instructions:
    screen.command(instr)
print(screen.lights_on())
print(screen)
