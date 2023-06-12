from gpiozero import SmoothedInputDevice

class MicrophoneSensor(SmoothedInputDevice):
    def __init__(self, pin=None, *, pull_up=False, active_state=None,
                 queue_len=5, sample_rate=100, threshold=0.5, partial=False,
                 pin_factory=None):
        super().__init__(
            pin, pull_up=pull_up, active_state=active_state,
            threshold=threshold, queue_len=queue_len,
            sample_wait=1 / sample_rate, partial=partial,
            pin_factory=pin_factory)
        self._queue.start()
    @property
    def value(self):
        return super().value    
    @property
    def sound_detected(self):
        return not self.is_active
MicrophoneSensor.when_sound = MicrophoneSensor.when_deactivated
MicrophoneSensor.when_no_sound = MicrophoneSensor.when_activated
MicrophoneSensor.wait_for_sound = MicrophoneSensor.wait_for_inactive
MicrophoneSensor.wait_for_no_sound = MicrophoneSensor.wait_for_active