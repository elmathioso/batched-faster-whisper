from faster_whisper import WhisperModel
import argparse
import glob
import shutil
import os

class Transcripter:

    def __init__(self):

        self.model_size = os.environ['WHISPER_MODEL']
        self.beam_size = int(os.environ['WHISPER_BEAM'])
        self.model = WhisperModel(self.model_size, device="cuda", compute_type="float16", download_root="/cache")


    def analyze_files(self, input_folder, output_location):


        for input_file in glob.glob(input_folder + "*.mp3"):

            try:
                print(input_file)

                # Load file info
                segments, info = self.model.transcribe(input_file, beam_size=self.beam_size)

                print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

                # start processing by forcing iterator
                segments = list(segments)
                segments = [x.text for x in segments]

                # Get filename + destination transcript
                filename = input_file.split('/')[-1].replace('.mp3', '')
                text = ".\n".join("\n".join(segments).split("."))
                with open(output_location + filename + ".txt", 'w', encoding='utf-8') as f:
                    f.write(text)
                print(filename)

                # move file once processed
                shutil.move(input_folder + filename + ".mp3", input_folder + 'Transcribed/' + filename + ".mp3")


            except Exception as e:
                print("Can't process " + input_file)
                print(e)


def main(input_location, output_location):

    # check location
    files = glob.glob(input_location + "*.mp3")
    if len(files) == 0:
        print("No files detected.")
    else:
        print("Found files:")
        print(files)
        t = Transcripter()
        t.analyze_files(input_location, output_location)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Transcripter')
    parser.add_argument('--input_location', help='The folder with the MP3 files to transcribe.')
    parser.add_argument('--output_location', help='The destination folder.')
#    parser.add_argument('--test', help='Run an initiation test. No output collected.', action='store_true', dest='test')
    args = parser.parse_args()
    print(args)

#    if args.test is not None:
#        tester(input_location=args.input_location)
#    else:
    main(input_location=args.input_location, output_location=args.output_location)
