# gpt-live-chat
For my Bavard Bar talk on A.I. - 26th July 2023

This waits for input on the microphone, performs speech-to-text, sends that text to the OpenAI chat API, takes the response and performs text-to-speech, saves the resulting mp3 to disk, and then runs that mp3 file through a media player. After each cycle, it will wait for an input from the command line (performed by pressing ```enter```), and then repeat the cycle until the program is killed.

By default, it uses the ```mpg321``` player.

You will need an OpenAI API key, and insert it where you see ```<<INSERT API KEY HERE>>```. Be careful not to share this key with anyone as the API is billed and misuse of you key will cost you money!