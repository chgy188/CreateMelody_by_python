#coding=utf8
from mido import Message,MetaMessage, MidiFile,MidiTrack,bpm2tempo
import random
#import sys
#chords = sys.argv[1]
#chords = [int(gpus.split(','))]
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

bpm = 86
tempo = bpm2tempo(bpm)
track.append(MetaMessage('time_signature', numerator=4, denominator=4))
track.append(MetaMessage('set_tempo', tempo = tempo, time=0))
track.append(MetaMessage('key_signature', key='C'))

chordlist=[60,62,64,65,67,69]
bigchord=[-5,0,4,7,12]
smallchord=[-5,0,3,7,12]
songseqs=[1,3,4,6,2,5]
for songseq in songseqs :
	print("song",songseq)
	#if songseq not in [1,2,3,4,5,6,7]: break
	segtimeseq=[]
	beats=0
	startbeat=4
	while beats<8:
		beatime=random.randint(1,startbeat)
		beats=beats+beatime
		if beats>8:
			beatime=beatime-(beats-8)
			beats=8
		#print(beats)
		startbeat=8-beatime
		segtimeseq.append(beatime)
	#print(segtimeseq)
	for segtime in segtimeseq:
		ran=random.randint(0,4)
		
		if songseq in [1,4,5]:
			n=chordlist[songseq-1]+bigchord[ran]
		else:
			n=chordlist[songseq-1]+smallchord[ran]
		t=240*segtime
		print(t)
		track.append(Message('program_change', program=1, time=0))
		track.append(Message('note_on', note=n, velocity=64, time=0))
		track.append(Message('note_on', note=n-5, velocity=64, time=0))
		track.append(Message('note_off', note=n, velocity=64, time=t))
		track.append(Message('note_off', note=n-5, velocity=64, time=t))




mid.save('song_by_py.mid')