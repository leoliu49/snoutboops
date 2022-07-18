import numpy as np
import time

from pysinewave import SineWave


def play_neurons(ts, nids, pitch_hi=30, pitch_lo=-5, timestep=0.1, zero_timestep=0.005):
    ts = np.array(ts)
    ts = ts - np.min(ts)            # start at time 0
    T = np.max(ts)
    assert(len(ts.shape) == 1)

    nids = np.array(nids)
    nids = nids - np.min(nids)      # start with neuron id 0
    max_nid = np.max(nids)
    assert(len(nids.shape) == 1)

    assert(ts.shape == nids.shape)

    pitch_range = pitch_hi - pitch_lo

    sinewave = SineWave(pitch=0, pitch_per_second=1000)
    sinewave.play()
    last_t = -1
    for i in range(ts.shape[0]):
        t = ts[i]; nid = nids[i]
        pitch = round(((nid/max_nid)*pitch_range) + pitch_lo, 2)
        print(t, nid, pitch)
        sinewave.set_pitch(pitch)
        dt = t - last_t
        last_t = t

        if dt == 0:
            time.sleep(zero_timestep)
        else:
            time.sleep(dt*timestep)

    sinewave.stop()
