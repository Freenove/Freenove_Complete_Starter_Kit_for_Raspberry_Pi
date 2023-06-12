from gpiozero import SmoothedInputDevice

class PhotoSensor(SmoothedInputDevice):
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
    def occlusion_detected(self):
        return not self.is_active
PhotoSensor.when_occlusion = PhotoSensor.when_deactivated
PhotoSensor.when_no_occlusion = PhotoSensor.when_activated
PhotoSensor.wait_for_occlusion = PhotoSensor.wait_for_inactive
PhotoSensor.wait_for_no_occlusion = PhotoSensor.wait_for_active
