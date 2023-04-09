# play star wars imperial march intro
import winsound

frequences = [
  392, 392, 392, 311, 466, 392, 311, 466, 392,
  587, 587, 587, 622, 466, 369, 311, 466, 392,
  784, 392, 392, 784, 739, 698, 659, 622, 659,
  415, 554, 523, 493, 466, 440, 466,
  311, 369, 311, 466, 392
]

durations = [
  350, 350, 350, 250, 200, 350, 250, 200, 700,
  350, 350, 350, 250, 100, 350, 250, 200, 700,
  350, 250, 200, 350, 250, 150, 150, 150, 450,
  150, 350, 250, 150, 150, 150, 450,
  150, 350, 250, 200, 750
]

# durations = map(lambda x: int(1.5*x), durations)
parameters = list(zip(frequences, durations))

for parameter in parameters:
  winsound.Beep(*parameter)

