from psychopy import visual, event, sound
from psychopy.core import StaticPeriod
import numpy as np
from pylsl import StreamInlet, StreamInfo, StreamOutlet, resolve_stream
import os

def runBlock(n_trials,n_blocks, stim_dur,stim_interval):
    
    #screensize = [1000, 1000]

    # create window#
    mywin = visual.Window(units='height' )#monitor="testMonitor") #units="deg")#, units='pix')
    
    #create stimuli
    message_lf = visual.TextStim(win=mywin, text='left foot')#, pos=[500,0])
    message_rf = visual.TextStim(win=mywin , text='right finger')#, pos=[500,0])
    message_start = visual.TextStim(win=mywin, text='Press any key to continue', pos=(0,0), units='norm')

 
    arrowVert_l = [(-0.2,0.05),(-0.2,-0.05),(0,-0.05),(0,-0.1),(0.2,0),(0,0.1),(0,0.05)]
    arrowVert_r = [(0.2,-0.05),(0.2,0.05),(0,0.05),(0,0.1),(-.2,0),(0,-0.1),(0,-0.05)]
    arrow_l = visual.ShapeStim(win=mywin, vertices=arrowVert_l, fillColor='white', size=.5, lineColor='white')
    arrow_r = visual.ShapeStim(win=mywin, vertices=arrowVert_r, fillColor='white', size=.5, lineColor='white')
    
    fixation = visual.ShapeStim(win=mywin, 
        vertices=((0, -0.05), (0, 0.05), (0,0), (-0.05,0), (0.05, 0)),
        lineWidth=2,
        closeShape=False,
        lineColor="white")

    #define stream
    info = StreamInfo(name='ErrP-Markers', type='Markers', channel_count=1,
                  nominal_srate=0, channel_format='string',
                  source_id='cybathlon_errp_markers')
    outlet = StreamOutlet(info)


    #main loop
    for block in range(n_blocks):

        #randomise presentation of stimuli before starting block  
        trials=np.random.choice([0, 1], size=(n_trials,))
        
        #start block after kepress
        message_start.draw()
        mywin.flip()
        event.waitKeys()

        #start block
        outlet.push_sample(['start_block'])
        for trial in trials:
            ISI = StaticPeriod(screenHz=60)
            ISI.start(stim_interval)
            fixation.draw()
            mywin.flip()
            outlet.push_sample(['fix'])
            ISI.complete()
            
            SI = StaticPeriod(screenHz=60)
            SI.start(stim_dur) 
            if trial ==1:
                arrow_l.draw()
                mywin.flip()
                beep = sound.Sound(os.path.join('figures', 'beep.wav'))
                beep.play()

                outlet.push_sample(['left'])
            else:
                arrow_r.draw()
                mywin.flip()
                outlet.push_sample(['right'])
            SI.complete()
        outlet.push_sample(['end_block'])
            
      
runBlock(3,2, 2,2)