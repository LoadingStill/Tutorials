import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os
import re
import threading


class VideoTranscoderGUI:
    def __init__(self, master):
        self.master = master
        master.title("Video Transcoder")
        master.minsize(400, 300)

        self.input_files = []
        self.output_dir = ""
        self.video_codec = tk.StringVar(value="libx264")
        self.audio_codec = tk.StringVar(value="aac")

        self.select_files_label = tk.Label(master, text="Choose video files:")
        self.select_files_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.select_files_button = tk.Button(master, text="Select Files", command=self.select_files)
        self.select_files_button.grid(row=0, column=1, padx=10, pady=10)

        self.output_dir_label = tk.Label(master, text="Choose output folder:")
        self.output_dir_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.output_dir_button = tk.Button(master, text="Select Output Directory", command=self.select_output_dir)
        self.output_dir_button.grid(row=1, column=1, padx=10, pady=10)

        self.video_codec_label = tk.Label(master, text="Video Codec:")
        self.video_codec_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.video_codec_menu = tk.OptionMenu(master, self.video_codec, "libx264", "libx265", "vp9", "libaom-av1", "h264_nvenc", "hevc_nvenc", "h264_amf", "hevc_amf")
        self.video_codec_menu.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.audio_codec_label = tk.Label(master, text="Audio Codec:")
        self.audio_codec_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.audio_codec_menu = tk.OptionMenu(master, self.audio_codec, "aac", "mp3", "opus")
        self.audio_codec_menu.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        self.transcode_button = tk.Button(master, text="Transcode", command=self.start_transcoding_thread)
        self.transcode_button.grid(row=4, column=1, padx=10, pady=10)

        self.cancel_button = tk.Button(master, text="Cancel", command=self.cancel_transcoding)
        self.cancel_button.grid(row=4, column=0, padx=10, pady=10)

        self.progress_bar = ttk.Progressbar(master, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.progress_bar.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W)

        self.percent_label = tk.Label(master, text="0%")
        self.percent_label.grid(row=5, column=1, pady=10)

    def cancel_transcoding(self):
        if hasattr(self, "process") and self.process.poll() is None:
            self.process.terminate()
            self.process.wait()
            messagebox.showinfo("Transcoding Canceled", "Transcoding process has been canceled.")
        else:
            self.master.destroy()

    def select_files(self):
        self.input_files = filedialog.askopenfilenames()

    def select_output_dir(self):
        self.output_dir = filedialog.askdirectory()

    def update_progress_bar(self, percent):
        self.progress_bar["value"] = percent
        self.percent_label.config(text=f"{percent:.0f}%")
        self.master.update_idletasks()

    def transcode(self):
        duration_regex = r"Duration: (\d{2}):(\d{2}):(\d{2}).(\d{2})"
        frame_regex = r"frame=\s*(\d+)"
        duration = 0
        for input_file in self.input_files:
            output_file = self.output_dir + "/" + os.path.splitext(os.path.basename(input_file))[0] + ".mp4"
            cmd = [
                "ffmpeg",
                "-hwaccel", "auto",
                "-i", input_file,
                "-c:v", self.video_codec.get(),
                "-c:a", self.audio_codec.get(),
                "-f", "mp4",
                "-y", output_file
            ]

            if self.video_codec.get() in ["h264_nvenc", "hevc_nvenc"]:
                cmd.insert(2, "-gpu")
                cmd.insert(3, "0")  # Change this to the index of the GPU you want to use (0 is the first GPU)

            if self.video_codec.get() in ["h264_amf", "hevc_amf"]:
                cmd.insert(2, "-opencl")
                cmd.insert(3, "1")  # Change this to the index of the OpenCL device you want to use (1 is the first GPU)

            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

            self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if "Duration" in output:
                    match = re.search(duration_regex, output)
                    if match:
                        duration = int(match.group(1)) * 3600 + int(match.group(2)) * 60 + int(match.group(3)) + float("0." + match.group(4))
                if "frame=" in output:
                    match = re.search(frame_regex, output)
                    if match:
                        frame = int(match.group(1))
                        percent = frame / (duration * 25) * 100  # assuming 25 fps
                        self.master.after(1, self.update_progress_bar, percent)

            self.progress_bar["value"] = 0

        messagebox.showinfo("Transcoding Complete", "All files have been transcoded.")

    def start_transcoding_thread(self):
        self.transcoding_thread = threading.Thread(target=self.transcode)
        self.transcoding_thread.start()


root = tk.Tk()
video_transcoder_gui = VideoTranscoderGUI(root)
root.mainloop()
