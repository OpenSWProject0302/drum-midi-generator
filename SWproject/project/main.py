from typing import Union
from pathlib import Path
import uuid
import logging
from mido import MidiFile
from midi.drum_generation import generate_drum_midi_from_audio

def main(audio_path: Union[str, Path], genre: str, tempo: int, level:str):
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    # MIDI 파일 이름 생성
    audio_path = Path(audio_path)
    name = audio_path.stem
    suffix = uuid.uuid4().hex[:6]
    filename = f"{name}_{suffix}.mid"

    # MIDI 파일 생성
    mid = MidiFile(ticks_per_beat=480)

    # 오디오에 맞는 드럼 track 생성 후 MIDI 파일에 추가
    drum_track = generate_drum_midi_from_audio(audio_path, genre, tempo, level)
    mid.tracks.append(drum_track)

    # MIDI 파일 저장
    mid.save(filename)
    logger.info(f"{filename} 파일이 생성되었습니다.")

if __name__ == "__main__":
    audio_path = "C:/Users/melte/Downloads/The_Ramones-Blitzkrieg_Bop.mp3"
    genre = "Punk rock"
    tempo = 176
    level = "Easy"
    
    main(audio_path, genre, tempo, level)