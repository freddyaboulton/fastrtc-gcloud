import os
import numpy as np
from fastrtc import ReplyOnPause, Stream, get_hf_turn_credentials


def detection(audio: tuple[int, np.ndarray]):
    # Implement any iterator that yields audio
    # See "LLM Voice Chat" for a more complete example
    yield audio


stream = Stream(
    handler=ReplyOnPause(detection),
    modality="audio",
    mode="send-receive",
    concurrency_limit=5,
    rtc_configuration=get_hf_turn_credentials,
    server_rtc_configuration=get_hf_turn_credentials(ttl=3_600 * 24 * 10),
    time_limit=90,
)

if __name__ == "__main__":
    stream.ui.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 8080)))
