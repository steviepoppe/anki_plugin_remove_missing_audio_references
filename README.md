# Anki Plugin: remove missing audio references

A small plugin to remove or replace all Anki notes references to audiofiles missing from the media collection, similar to Anki's "remove empty cards" function.

## Purpose

This plugin will probably mainly be used by Japanese learners having [set up rikaisama with anki](http://steviepoppe.net/blog/2016/09/a-quick-guide-on-using-anki-2-an-efficient-vocab-mining-set-up-with-anki-and-rikaisama/) to import anki cards containing Japanese-pod101's audiofiles. Ocassionally, idioms or less used words have no matched audio recordings available, yet importing a new card will contain a soundfile reference regardless if the actual audiofile exists. When building cards based on oral recognition, this results in empty cards. 

To automatize the removal process, this plugin removes all audio references, leaving oral recognition cards with an empty front-side (easily removed by clicking *Tools* -> *Empty Cards*). The plugin however is broad enough to be used in other contexts in which references to missing audio files have to be removed or replaced with another string. 

## Download

Install by copy-pasting `1328067109` into Anki's desktop program.

* [This plugin's Anki page](https://ankiweb.net/shared/info/1328067109)

## Usage

To replace references to missing audio files to something else, just change the value of the `REPLACE_STRING` string in `Remove_Absent_Audio.py`.

## License

Remove_Absent_Audio is licensed under [GNU GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html), as provided in the LICENSE file.
