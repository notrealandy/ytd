import os
import subprocess

def download_video(url, download_path):
    try:
        download_path = os.path.expanduser(download_path)

        if not os.path.exists(download_path):
            print(f"Directory {download_path} does not exist. Creating it...")
            os.makedirs(download_path)

        print(f"Downloading: {url} to {download_path}...")

        command = [
            'yt-dlp',
            '-f', 'bv*+ba/best',
            '-o', os.path.join(download_path, '%(title)s.%(ext)s'),
            '--recode-video', 'mp4',
            url
        ]

        subprocess.run(command, check=True)

        print(f"Download complete and saved in {download_path}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while downloading: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    default_path = '~/Downloads'

    print("\n")
    print("""
     ██    ██ ████████ ██████ 
      ██  ██     ██    ██   ██
       ████      ██    ██   ██     YouTube Downloader
        ██       ██    ██   ██     @notrealandy
        ██       ██    ██████
    """)
    print("\n")
    print(f"\33[1mDefault path:\33[0m \33[32m\33[3m\33[7m{os.path.expanduser(default_path)}\33[0m")
    path_input = input("Enter path to save video or press \33[1m'ENTER'\33[0m to use \33[1mdefault\33[0m:\33[0m\n>> ").strip()
    if path_input == '':
        print("\n")
        print(f"\33[90mUsing default path: {os.path.expanduser(default_path)}\33[0m")
    else:
        print("\n")
        print(f"\33[90mUsing input path: {os.path.expanduser(path_input)}\33[0m")
    path_to_use = path_input if path_input else default_path

    video_url = input("Paste the YouTube video URL:\n>> ").strip()

    if not video_url:
        print("\n")
        print("No URL provided. Exiting.")
    else:
        print("\n")
        download_video(video_url, path_to_use)
