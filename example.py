import resampy
import soundfile

from svr_tts import SVR_TTS
from svr_tts.core import SynthesisInput

if __name__ == '__main__':
    tts = SVR_TTS(api_key="some_key")
    wave, sr = soundfile.read('tmp/example.ogg')
    wave_24k = resampy.resample(wave, sr, 24_000)
    waves_22050 = tts.synthesize_batch([
        SynthesisInput(text="Сбейте лестницу!", stress=True, timbre_wave_24k=wave_24k, prosody_wave_24k=wave_24k),
    ])
    soundfile.write('tmp/example.wav', waves_22050[0], 22_050)
