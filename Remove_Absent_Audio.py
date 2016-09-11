# -*- mode: Python ; coding: utf-8 -*-
#
# https://github.com/steviepoppe/anki_plugin_remove_missing_audio_references
# License: GNU GPL 3.0, https://www.gnu.org/licenses/gpl-3.0.en.html
# Authors: Stevie Poppe
#
# Description: A small plugin to remove or replace all Anki notes references to audiofiles missing from the media collection

from aqt import mw
from aqt.utils import saveGeom, restoreGeom, showInfo, showWarning, \
    restoreState, getOnlyText, askUser, applyStyles, showText, tooltip, \
openHelp, openLink, checkInvalidFilename
from aqt.qt import *

import os
import sys
import re

REPLACE_STRING = ""

def remAbsent():
	mw.window().progress.start(immediate=True)
	absent_sounds = findAllAbsent()
	if not absent_sounds:
		mw.window().progress.finish()
		tooltip(_("No absent audio references."))
		return

	report = absentAudioReport(absent_sounds)
	mw.window().progress.finish()

	part1 = ngettext("%d absent audio reference", "%d absent audio references", len(absent_sounds)) % len(absent_sounds)
	part1 = _("%s to remove:") % part1
	diag, box = showText(part1 + "\n\n" + report, run=False, geomKey="absentAudio")
	box.addButton(_("Remove Audio Reference"), QDialogButtonBox.AcceptRole)
	box.button(QDialogButtonBox.Close).setDefault(True)
	def onDelete():
		saveGeom(diag, "absentAudio")
		QDialog.accept(diag)
		mw.window().checkpoint(_("Remove Absent Audio Reference"))
		remove_references(absent_sounds)
		tooltip(ngettext("%d reference removed.", "%d references removed.", len(absent_sounds)) % len(absent_sounds))
		mw.window().reset()
	box.accepted.connect(onDelete)
	diag.show()

def absentAudioReport(absent_sounds):
	rep = ""
	for absent_sound in absent_sounds:
		rep += _("Audiofile: [sound: %s]\n") % absent_sound[2]

	return rep

def findAllAbsent():
	L = []
	nids = mw.col.db.list("select id from notes")
	for nid in nids:
		n = mw.col.getNote(nid)
		for (name, value) in n.items():
			sounds = re.findall(r'\[sound:(.*?)\]', value)
			for sound in sounds:
				if sound:
					if not os.path.exists(os.path.join(mw.col.media.dir(), sound)):
						L.append([nid, name, sound])
	return L

def remove_references(absent_sounds):
	for absent_sound in absent_sounds:
		n = mw.col.getNote(absent_sound[0])		
		n[absent_sound[1]] = n[absent_sound[1]].replace("[sound:" + absent_sound[2] +"]", REPLACE_STRING)
		n.flush()

action = QAction("Remove Absent Audio References", mw)

mw.connect(action, SIGNAL("triggered()"), remAbsent)

mw.form.menuTools.addAction(action)



