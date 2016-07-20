from modules import midiProxy
from modules import kerasProxy
from modules import audio

def loadFolder(path):
	for root, dirs, files in os.walk("./samples/mididatabase/files.mididatabase.com/rock/metallica"):
	    for idx, file in enumerate(files):
	        if file.endswith(".mid"):
	            print(os.path.join(root, file))
	            songs.append(loadMidiDrums(os.path.join(root, file)))


midi = midiProxy.loadMidiDrums("../../Data/samples/tabs/LegionsOfTheSerpent.mid")
wave = audio.load("../../Data/samples/tabs/LegionsOfTheSerpent.wav")
samplingRate, spectrogram = audio.performFFTs(wave, frameDuration=0.1, windowStep=0.05)

print samplingRate, spectrogram.shape
audio.visualizeArray(spectrogram)
# numFeatures = len(songs[0][0]) if songs else 9
# model = getLSTMModel(maxLength, numFeatures)
# testModel(model, maxLength)
# 
# if os.path.isfile('LSTMTest.h5'): 
#     model.load_weights('LSTMTest.h5')
# 
# for idx, song in enumerate(songs):
#     trainModel(model, song, maxLength)
#     print str(idx) + " trained"
#     model.save_weights('LSTMTest.h5')
#     testModel(model, maxLength)