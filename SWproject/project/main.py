from typing import Union
from pathlib import Path
import logging
from midi.midi_writer import create_midi_path, write_midi
from midi.drum_generation import generate_drum_midi_from_audio
from midi.midi_converter import convert_midi
from audio.separation_mix import separate_merge_drum

def main(audio_path: Union[str, Path], genre: str, tempo: int, level:str, output_dir=None):
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

    audio_path = Path(audio_path)
    
    # 1. MIDI 파일 경로 생성
    midi_path = create_midi_path(audio_path, output_dir)

    # 2. 드럼 MIDI 생성
    drum_track = generate_drum_midi_from_audio(audio_path, genre, tempo, level)
    
    # 3. MIDI 저장
    write_midi(drum_track, midi_path)
    logger.info(f"{midi_path.stem}.mid 파일이 생성되었습니다.")

    # 4. PDF, 드럼 오디오 파일 변환 (output_dir 추가 가능)
    pdf_path, drum_audio_path = convert_midi(midi_path)
    
    # 5. 원곡과 드럼 오디오 병합 (output_dir 추가 가능)
    mix_audio_path = separate_merge_drum(audio_path, drum_audio_path)

    return pdf_path, drum_audio_path, mix_audio_path, midi_path

if __name__ == "__main__":
    audio_path = r"C:\Users\melte\OneDrive\바탕 화면\L.H.N\1. School\3-2\공개SW프로젝트\The_Ramones-Blitzkrieg_Bop.mp3"
    genre = "Rock" # 
    tempo = 176
    level = "Normal" # "Easy"
    
    main(audio_path, genre, tempo, level)