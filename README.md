# Mediamover
A python script to help sort files downloaded by a torrent client, into the respective files or folders:
for example: ~/SeriesName/Season #/file

Sorts all other files into an alternative folder, called 'Movies'
Saves successful filemoves to a log file, and lastly, if there are duplicates, moves files to a Mediadump folder, to be inspected later.

Script is run by 'Automator' as a 'Folder Action' workflow on OSX, or by Task Scheduler on Windows. Automator script is included.
