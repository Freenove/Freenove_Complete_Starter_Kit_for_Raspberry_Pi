from gpiozero import SmoothedInputDevice

class InfraredSensor(SmoothedInputDevice):
    def __init__(self, pin=None, *, pull_up=True, active_state=None,
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
    def reflect_detected(self):
        return not self.is_active
InfraredSensor.when_reflect = InfraredSensor.when_activated
InfraredSensor.when_no_reflect = InfraredSensor.when_deactivated
InfraredSensor.wait_for_reflect = InfraredSensor.wait_for_inactive
InfraredSensor.wait_for_no_reflect = InfraredSensor.wait_for_active
