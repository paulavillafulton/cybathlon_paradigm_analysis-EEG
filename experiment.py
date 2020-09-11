from psychopy import visual, event, sound, core
from psychopy.core import StaticPeriod
import numpy as np
from pylsl import StreamInlet, StreamInfo, StreamOutlet, resolve_stream
import os, random

duration = {
    'motor': 3.5,
    'beep':1 ,
    'break':1,
    'cue': 1.5
}

motors = [
    'hand',
    'foot',
    'breathe',
    'word',
    'rotate',
    'taste',
    'subs',
    'spatial',
    'auditory'
]

path_motors = {}

for m in motors:
    path_motors[m] = os.path.join('figures', m + '.png')

# for one paradigm, show the cue, motor imagery, break
def run_block(window, motor, motor_path, markerstream):
    fixation = visual.ShapeStim(win=window,
        vertices=((0, -0.05), (0, 0.05), (0,0), (-0.05,0), (0.05, 0)),
        lineWidth=2,
        closeShape=False,
        lineColor="white")
    motor_imagery = visual.ImageStim(window, motor_path)
    #cue
    ISI = StaticPeriod(screenHz=60)
    ISI.start(duration['cue'])
    motor_imagery.draw()
    window.flip()
    markerstream.push_sample(['cue_'+motor])
    ISI.complete()
    #imagery
    ISI = StaticPeriod(screenHz=60)
    ISI.start(duration['motor'])
    fixation.draw()
    window.flip()
    markerstream.push_sample(['imagery_'+motor])
    ISI.complete()

    #break
    ISI = StaticPeriod(screenHz=60)
    ISI.start(duration['break'])
    window.flip()
    markerstream.push_sample(['break'])
    ISI.complete()

def inter_set_break(mywin, seconds):
    ISI = StaticPeriod(screenHz=60)
    ISI.start(seconds)
    message_break = visual.TextStim(win=mywin, text= f'Break for {seconds} seconds', pos=(0, 0), units='norm')
    message_break.draw()
    mywin.flip()
    #TODO timer
    ISI.complete()

#def trial
def run_set(mywin, motor_imageries, num_trials):
    # create window#
    message_start = visual.TextStim(win=mywin, text='Experiment starts after Beep, press any key to continue', pos=(0,0), units='norm')

    message_start.draw()
    mywin.flip()
    event.waitKeys()

    #define stream
    info = StreamInfo(name='MI-Markers', type='Markers', channel_count=1,
                  nominal_srate=0, channel_format='string',
                  source_id='cybathlon_MI_markers')
    markerstream = StreamOutlet(info)

    #load sound
    beep = sound.Sound(os.path.join('figures', 'beep.wav'))

    #starts trial
    for n in range(num_trials):
        # shuffle order
        random.shuffle(motor_imageries)
        ISI = StaticPeriod(screenHz=60)
        ISI.start(1)
        beep.play()
        markerstream.push_sample(['beep'])
        ISI.complete()

        for motor in motor_imageries:
            run_block(mywin, motor, path_motors[motor], markerstream)



def run_experiment():
    num_trials = 10
    mywin = visual.Window(units='height', fullscr =  True)  # monitor="testMonitor") #units="deg")#, units='pix')

    # TODO: randomization: let the paradigms appear repeated?
    run_set(mywin, ['hand', 'foot', 'subs', 'breathe'], num_trials = num_trials)
    inter_set_break(mywin, 5)
    run_set(mywin, ['hand', 'spatial', 'word', 'breathe'], num_trials = num_trials )
    inter_set_break(mywin, 5)
    run_set(mywin, ['rotate', 'auditory', 'taste', 'breathe'], num_trials = num_trials)

    message_end = visual.TextStim(win=mywin, text='Thanks for participation!', pos=(0, 0), units='norm')
    message_end.draw()
    mywin.flip()
    event.waitKeys()


#def trial
def run_pair(mywin, motor_imageries, num_trials):
    # create window#
    message_start = visual.TextStim(win=mywin, text='Experiment starts after Beep, press any key to continue', pos=(0,0), units='norm')

    message_start.draw()
    mywin.flip()
    event.waitKeys()

    #define stream
    info = StreamInfo(name='MI-Markers', type='Markers', channel_count=1,
                  nominal_srate=0, channel_format='string',
                  source_id='cybathlon_MI_markers')
    markerstream = StreamOutlet(info)

    #load sound
    beep = sound.Sound(os.path.join('figures', 'beep.wav'))

    ISI = StaticPeriod(screenHz=60)
    ISI.start(1)
    beep.play()
    markerstream.push_sample(['beep'])
    ISI.complete()

    #starts trial
    for n in range(num_trials):
        # shuffle order
        random.shuffle(motor_imageries)


        for motor in motor_imageries:
            run_block(mywin, motor, path_motors[motor], markerstream)



def run_paired_expreiment():
    mywin = visual.Window(units='height', fullscr =  False)  # monitor="testMonitor") #units="deg")#, units='pix')

    num_trials = 30
    # TODO: randomization: let the paradigms appear repeated?
    run_pair(mywin, ['hand', 'foot'], num_trials = num_trials)
    inter_set_break(mywin, 5)
    # motor vs. abstract 
    run_pair(mywin, ['hand', 'subs'], num_trials = num_trials )
    run_pair(mywin, ['hand', 'rotate'], num_trials = num_trials )
    run_pair(mywin, ['hand', 'auditory'], num_trials = num_trials )

    inter_set_break(mywin, 5)
    #motor vs. multimodal
    run_pair(mywin, ['hand', 'spatial'], num_trials = num_trials)
    run_pair(mywin, ['hand', 'taste'], num_trials =  num_trials )
    run_pair(mywin, ['hand', 'word'], num_trials = num_trials )

    #run_pair(mywin, ['hand', 'breathe'], num_trials = num_trials )

    message_end = visual.TextStim(win=mywin, text='Thanks for participation!', pos=(0, 0), units='norm')
    message_end.draw()
    mywin.flip()
    event.waitKeys()


#run_experiment()
run_paired_expreiment()