import sys
import pyttsx3

if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        text = file.read()
        lines = [i for i in text.splitlines() if i != ' ' and len(i) > 0]
    engine = pyttsx3.init()
    if len(sys.argv) > 2:
        line_number = int(sys.argv[2])
    else:
        line_number = 0
    for index, line in enumerate(lines):
        print(index, line)
        if index >= line_number:
            try:
                engine.say(line)
                engine.runAndWait()
            except KeyboardInterrupt:
                print(index)
                break
