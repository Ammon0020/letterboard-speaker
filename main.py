import pygame
import json

# try to load the list of example wav filepaths and keys.
# if the json doesn't exist, create it
try:
    sounds = json.load(open("sounds.json"))
except:
    json.dump([], open("sounds.json", "w"))
    sounds = []

# if the json is empty, write an example dictionary
if len(sounds) == 0:
    sounds = [
        {"file": "sounds/a.wav", "key": "a"},
        {"file": "sounds/b.wav", "key": "b"},
        {"file": "sounds/c.wav", "key": "c"},
        {"file": "sounds/d.wav", "key": "d"},
        {"file": "sounds/e.wav", "key": "e"},
        {"file": "sounds/f.wav", "key": "f"},
        {"file": "sounds/g.wav", "key": "g"},
        {"file": "sounds/h.wav", "key": "h"},
        {"file": "sounds/i.wav", "key": "i"},
        {"file": "sounds/j.wav", "key": "j"},
        {"file": "sounds/k.wav", "key": "k"},
        {"file": "sounds/l.wav", "key": "l"},
        {"file": "sounds/m.wav", "key": "m"},
        {"file": "sounds/n.wav", "key": "n"},
        {"file": "sounds/o.wav", "key": "o"},
        {"file": "sounds/p.wav", "key": "p"},
        {"file": "sounds/q.wav", "key": "q"},
        {"file": "sounds/r.wav", "key": "r"},
        {"file": "sounds/s.wav", "key": "s"},
        {"file": "sounds/t.wav", "key": "t"},
        {"file": "sounds/u.wav", "key": "u"},
        {"file": "sounds/v.wav", "key": "v"},
        {"file": "sounds/w.wav", "key": "w"},
        {"file": "sounds/x.wav", "key": "x"},
        {"file": "sounds/y.wav", "key": "y"},
        {"file": "sounds/z.wav", "key": "z"},

    ]
    json.dump(sounds, open("sounds.json", "w"))


# init pygame
pygame.init()
size = (250, 250)
screen = pygame.display.set_mode(size)

# init mixer
pygame.mixer.init()
print("channel cnt", pygame.mixer.get_num_channels())  # max track count (8 on my machine)

# main loop
while True:
    pygame.time.Clock().tick(10)

    # check for quit (X button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # check for key press
    idx = 0
    keys = pygame.key.get_pressed()

    # check for key press
    # if keys[pygame.K_1]: idx = 1
    # if keys[pygame.K_2]: idx = 2
    for sound in sounds:
        key = sound.get('key') # sound.get('key') returns the literal key value (e.g. '1')
        if keys[pygame.key.key_code(key)]:
            idx = sounds.index(sound) + 1

    # play sound
    if (idx):
        ch = pygame.mixer.find_channel()  # find open channel, returns None if all channels used
        snd = pygame.mixer.Sound(sounds[idx - 1].get('file'))  # create sound object, must be wav or ogg
        if (ch): ch.play(snd)  # play on channel if available
