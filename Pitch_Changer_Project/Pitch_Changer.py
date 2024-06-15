from pydub import AudioSegment
from shutil import move

def ChangePitch(input_file,output_file,semitones):
    voice = AudioSegment.from_file(input_file)
    voice_with_altered_pitch = voice._spawn(voice.raw_data,overrides={
        "frame_rate": int(voice.frame_rate * (2 ** (semitones / 12)))
    })
    voice_with_altered_pitch.export(output_file,format="wav")

i = input("Enter the name of input file: ")
i_2 = input("Enter the name of output file: ")
i_3 = input("Enter the semitones (semitones must be integer): ")

input_file = f"Records/{str(i)}"
output_file = f"{str(i_2)}"
semitones = int(i_3)

ChangePitch(input_file,output_file,semitones)
move(output_file,"Outputs")
